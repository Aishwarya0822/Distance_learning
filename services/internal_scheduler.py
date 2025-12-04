import threading
import time
import logging
from django.utils import timezone
from django.db import connection
from .google_drive_service import GoogleDriveService
from .sync_service import DriveSyncService

logger = logging.getLogger(__name__)

RUN_EVERY_SECONDS = 600  # 10 minutes = 600 seconds
_scheduler_started = False
_scheduler_thread = None
_scheduler_stop_event = threading.Event()

def start_drive_sync_scheduler():
    """
    Start a background thread that calls sync_all_folders() every 10 minutes.
    This is triggered once when Django app is ready.
    """
    global _scheduler_started, _scheduler_thread, _scheduler_stop_event
    
    if _scheduler_started:
        logger.warning("Scheduler already started, skipping...")
        return
    
    _scheduler_started = True
    _scheduler_stop_event.clear()

    def sync_job():
        """The actual sync job that runs every 10 minutes"""
        try:
            logger.info("=" * 50)
            logger.info(f"DRIVE SYNC SCHEDULER STARTED: {timezone.now()}")
            logger.info("Running Google Drive sync...")
            
            # Ensure database connection is fresh
            connection.close()
            
            drive = GoogleDriveService()
            sync = DriveSyncService(drive)
            sync.sync_all_folders()
            
            logger.info(f"DRIVE SYNC COMPLETED: {timezone.now()}")
            logger.info("=" * 50)
            
        except ImportError as e:
            logger.error(f"Import error in sync job: {e}")
        except Exception as e:
            logger.error(f"DRIVE SYNC ERROR: {e}", exc_info=True)
            logger.info(f"Next sync attempt in {RUN_EVERY_SECONDS} seconds")

    def scheduler_loop():
        """Main scheduler loop"""
        logger.info(f"Starting scheduler loop, interval: {RUN_EVERY_SECONDS} seconds")
        
        while not _scheduler_stop_event.is_set():
            try:
                sync_job()
            except Exception as e:
                logger.error(f"SCHEDULER LOOP ERROR: {e}", exc_info=True)
            
            # Wait for the specified interval or until stop event
            _scheduler_stop_event.wait(RUN_EVERY_SECONDS)

    # Start the scheduler thread
    _scheduler_thread = threading.Thread(
        target=scheduler_loop, 
        daemon=True,
        name="GoogleDriveSyncScheduler"
    )
    _scheduler_thread.start()
    
    logger.info(f"Google Drive Sync Scheduler started! Running every {RUN_EVERY_SECONDS} seconds")

def stop_drive_sync_scheduler():
    """Stop the scheduler (for testing/development)"""
    global _scheduler_started, _scheduler_thread, _scheduler_stop_event
    
    if _scheduler_started:
        logger.info("Stopping Google Drive Sync Scheduler...")
        _scheduler_stop_event.set()
        _scheduler_started = False
        
        if _scheduler_thread and _scheduler_thread.is_alive():
            _scheduler_thread.join(timeout=10)  # Wait up to 10 seconds for thread to finish
            if _scheduler_thread.is_alive():
                logger.warning("Scheduler thread did not stop gracefully")
        logger.info("Google Drive Sync Scheduler stopped")
    else:
        logger.info("Scheduler was not running")

def is_scheduler_running():
    """Check if scheduler is running"""
    return _scheduler_started and _scheduler_thread and _scheduler_thread.is_alive()

def get_scheduler_status():
    """Get scheduler status information"""
    return {
        'running': is_scheduler_running(),
        'interval_seconds': RUN_EVERY_SECONDS,
        'next_sync_in': 'Unknown'
    }
