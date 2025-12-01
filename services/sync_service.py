# super_admin/services/sync_service.py
import re
from django.utils import timezone
from django.db import transaction
from dateutil.parser import isoparse

from student_management.models import CallRecording, DriveFolder, SyncLog
from .google_drive_service import GoogleDriveService


def extract_phone(name: str) -> str | None:
    """
    Try to find a 10–12 digit phone number in the filename.
    Example: 'call_9876543210_2025-11-10.m4a'
    """
    m = re.search(r"\b(\+?\d{10,12})\b", name or "")
    return m.group(1) if m else None


def parse_drive_datetime(dt_str):
    """Parse Google Drive ISO datetime into aware Django datetime."""
    try:
        dt = isoparse(dt_str)
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt
    except Exception:
        return timezone.now()


class DriveSyncService:
    """
    Service that syncs Google Drive audio files metadata only
    No file downloading - only stores file references
    """

    def __init__(self, drive_service: GoogleDriveService):
        self.drive = drive_service

    def sync_single_folder(self, folder: DriveFolder):
        """Sync one Drive folder into CallRecording table (metadata only)."""
        print(f"➡️  Sync started for folder: {folder.name} ({folder.folder_id})")
        log = SyncLog.objects.create(folder=folder)
        found = 0
        added = 0
        updated = 0

        try:
            for f in self.drive.iter_all_audio_files(folder.folder_id):
                found += 1

                drive_file_id = f["id"]
                name = f.get("name") or ""
                phone = extract_phone(name) or ""
                created_dt = (
                    parse_drive_datetime(f.get("createdTime"))
                    if f.get("createdTime")
                    else timezone.now()
                )
                size = int(f.get("size") or 0)
                link = self.drive.file_web_link(f)

                with transaction.atomic():
                    obj, created_obj = CallRecording.objects.get_or_create(
                        google_drive_file_id=drive_file_id,
                        defaults={
                            "user_id": folder.user_id,
                            "phone_number": phone,
                            "drive_file_name": name,
                            "file_name": name,
                            "file_size": size,
                            "google_drive_link": link,
                            "status": "synced",
                            "recording_date": created_dt,
                            "last_synced_at": timezone.now(),
                        },
                    )

                    if created_obj:
                        added += 1
                        print(f"✅ Added new recording: {name}")
                    else:
                        update_fields = []

                        if obj.user_id != folder.user_id:
                            obj.user_id = folder.user_id
                            update_fields.append("user_id")
                        if obj.drive_file_name != name:
                            obj.drive_file_name = name
                            update_fields.append("drive_file_name")
                        if obj.file_name != name:
                            obj.file_name = name
                            update_fields.append("file_name")
                        if obj.file_size != size:
                            obj.file_size = size
                            update_fields.append("file_size")
                        if link and obj.google_drive_link != link:
                            obj.google_drive_link = link
                            update_fields.append("google_drive_link")
                        if not obj.phone_number and phone:
                            obj.phone_number = phone
                            update_fields.append("phone_number")
                        if obj.status != "synced":
                            obj.status = "synced"
                            update_fields.append("status")

                        if update_fields:
                            obj.last_synced_at = timezone.now()
                            update_fields.append("last_synced_at")
                            update_fields.append("updated_at")
                            obj.save(update_fields=update_fields)
                            updated += 1
                            print(f"🔄 Updated recording: {name}")

            log.sync_completed_at = timezone.now()
            log.total_files_found = found
            log.new_files_added = added
            log.status = "success"
            log.save()

            print(
                f"✅ Sync success for folder: {folder.name} | "
                f"found={found}, new={added}, updated={updated}"
            )

        except Exception as e:
            log.sync_completed_at = timezone.now()
            log.total_files_found = found
            log.new_files_added = added
            log.status = "failed"
            log.error_message = str(e)
            log.save()

            print(f"❌ Sync FAILED for folder: {folder.name} | error={e}")
            raise

    def sync_all_folders(self):
        """Sync all active folders (metadata only)."""
        print("🔄 sync_all_folders() — fetching active DriveFolder entries...")
        folders = DriveFolder.objects.filter(is_active=True)

        if not folders.exists():
            print("⚠️  No active DriveFolder found. Nothing to sync.")
            return

        total_folders = folders.count()
        print(f"📁 Found {total_folders} active folders to sync")

        for i, folder in enumerate(folders, 1):
            try:
                print(f"🔄 Syncing folder {i}/{total_folders}: {folder.name}")
                self.sync_single_folder(folder)
            except Exception as e:
                print(f"⚠️  Failed to sync folder {folder.name}: {e}")
                continue

        print("✅ sync_all_folders() finished.")
