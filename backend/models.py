from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class OrganizationProfile(AbstractUser):
    org_name = models.CharField(max_length=10000)
    email = models.CharField(max_length=225, unique=True)
    username = None
    password = models.CharField(max_length=225)
    org_profileImg = models.ImageField(upload_to='uploads/org_profile', blank=False)
    org_address = models.TextField(max_length=1000, blank=False)
    # date_registered = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.org_name

class ApplicationData(models.Model):
    organization = models.ForeignKey(OrganizationProfile, on_delete=models.CASCADE)
    org_id = models.IntegerField()
    firstname = models.CharField(max_length=1000, blank=False, null=False)
    lastname = models.CharField(max_length=1000, blank=False, null=False)
    othername = models.CharField(max_length=1000, blank=False, null=False)
    email = models.CharField(max_length=1000, blank=False, null=False)
    phone_number = models.CharField(max_length=1000, blank=False, null=False)
    gender = models.CharField(max_length=1000, blank=False, null=False)
    contact_address = models.CharField(max_length=1000, blank=False, null=False)
    nin_number = models.IntegerField(blank=False, null=False)
    qualification = models.CharField(max_length=1000, blank=True, null=True)
    job_history = models.CharField(max_length=1000, blank=True, null=True)
    cover_letter = models.FileField(upload_to='uploads/documents', blank=True)
    resume = models.FileField(upload_to='uploads/documents', blank=True)
    ref_fullname = models.CharField(max_length=1000, blank=False, null=False)
    ref_phone_number = models.CharField(max_length=1000, blank=False, null=False)
    ref_address = models.CharField(max_length=1000, blank=False, null=False)
    work_auth = models.CharField(max_length=1000, blank=True, null=True)
    salary_exp = models.CharField(max_length=1000, blank=True, null=True)
    availabilty = models.CharField(max_length=1000, blank=True, null=True)
    skills = models.CharField(max_length=1000, blank=True, null=True)
    doc_files = models.FileField(upload_to='uploads/documents', blank=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname, self.lastname

