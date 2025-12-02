from django.db import models
from student_management.models import *
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

#---------------job portal--------------------------------------

class JobSeekerProfile(models.Model):
    WORK_STATUS_CHOICES = [
        ("experienced", "I'm experienced"),
        ("fresher", "I'm a fresher"),
        ("student", "I'm a student"),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES, blank=True, null=True)
    city=models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"

    class Meta:
        db_table = 'jobseeker_profile'

class JobSeekerEducation(models.Model):
    COURSE_TYPE_CHOICES = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    education_details = models.JSONField(default=list)
    key_skills = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)  # Only this
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} Education"

    class Meta:
        db_table = 'jobseeker_education'

class JobSeekerEmploymentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employment_history')
    is_currently_employed = models.BooleanField(default=False)
    total_work_exp_years = models.IntegerField(default=0)
    total_work_exp_months = models.IntegerField(default=0)
    company_name = models.CharField(max_length=200, default="")
    current_job_title = models.CharField(max_length=100, default="")
    current_city = models.CharField(max_length=100, default="")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current_job = models.BooleanField(default=False)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notice_period = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.company_name}"

    class Meta:
        db_table = 'jobseeker_employmentdetails'

class JobSeekerWorkPreferences(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_preferences')
    preferred_locations = models.JSONField(default=list, help_text="List of up to 10 preferred locations")
    preferred_salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} Preferences"

    class Meta:
        db_table = 'jobseeker_workpreferences'

class JobSeekerApplication(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("viewed", "Viewed"),
        ("shortlisted", "Shortlisted"),
        ("interviewing", "Interviewing"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    job_post = models.ForeignKey('JobPost', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='job_applications/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="applied")
    application_date = models.DateTimeField(auto_now_add=True)
    last_status_change = models.DateTimeField(auto_now=True)
    resume_viewed = models.BooleanField(default=False)
    resume_viewed_at = models.DateTimeField(null=True, blank=True)
    application_viewed = models.BooleanField(default=False)
    application_viewed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'job_post')
        db_table = 'jobseeker_application'

    def __str__(self):
        return f"{self.user.get_full_name()} applied for {self.job_post.job_title}"

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def mark_resume_viewed(self):
        if not self.resume_viewed:
            self.resume_viewed = True
            self.resume_viewed_at = timezone.now()
            self.save()

    def update_status(self, new_status):
        if new_status not in dict(self.STATUS_CHOICES).keys():
            raise ValueError("Invalid status provided")
        self.status = new_status
        self.last_status_change = timezone.now()
        self.save()


class Job_Portal_AdditionalBenefit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Job_Portal_Qualification(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Job_Portal_Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Job_Portal_RequiredSkill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Job_Portal_Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "industry"
        ordering = ["name"]

    def __str__(self):
        return self.name

class JobPost(models.Model):
    company_name = models.CharField(max_length=250)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    min_experience = models.IntegerField(null=True, blank=True)
    max_experience = models.IntegerField(null=True, blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    industry_ids = models.JSONField(default=list)  
    qualification_ids = models.JSONField(default=list)
    additional_benefit_ids = models.JSONField(default=list)
    department_id = models.IntegerField(null=True, blank=True)
    required_skill_ids = models.JSONField(default=list)
    language_ids = models.JSONField(default=list)

    # NEW FIELDS
    responsibilities = models.JSONField(default=list, blank=True)  # list[str]
    requirements = models.JSONField(default=list, blank=True)      # list[str]

    gender_preference = models.CharField(
        max_length=20,
        choices=[("Any", "Any"), ("Male", "Male"), ("Female", "Female")],
        default="Any"
    )
    screening_questions = models.JSONField(default=list, blank=True)
    job_description = models.TextField()
    allow_direct_calls = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        db_table = 'jobpost'
        



