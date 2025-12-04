# distance_learning/config.py
import os

# Client Configuration - Change this for different deployments
# CLIENT_CONFIG = os.getenv('REQUIRES', 'BOTH')  # Options: 'STUDENT_ONLY', 'JOB_ONLY', 'BOTH'


CLIENT_CONFIG = 'BOTH'

def get_enabled_apps():
    if CLIENT_CONFIG == 'STUDENT_ONLY':
        return ['student_management']
    elif CLIENT_CONFIG == 'JOB_ONLY':
        return ['student_management', 'job_portal']  # Always include student_management
    else:  # BOTH
        return ['student_management', 'job_portal']

def get_auth_model():
    return 'student_management.User'  # Always use custom User

def is_feature_enabled(feature):
    if CLIENT_CONFIG == 'STUDENT_ONLY':
        return feature == 'student_management'
    elif CLIENT_CONFIG == 'JOB_ONLY':
        return feature == 'job_portal'
    else:
        return True

