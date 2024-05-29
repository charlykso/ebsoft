from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    engagement_model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} --------------------- {self.subject} --------------------- {self.created_at}"


class UserAplication(models.Model):
    fullname = models.CharField(max_length=160)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=100)
    current_location = models.CharField(max_length=160)
    current_company = models.CharField(max_length=160)
    notice_period = models.CharField(max_length=100)
    salary_expectation = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    referral_source = models.CharField(max_length=200)
    years_of_experience = models.CharField(max_length=50)
    cv = models.BooleanField(default=False)
    linkedin_profile = models.URLField(max_length=500)
    github_profile = models.URLField(max_length=500)
    portfolio = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"{self.lastname} {self.firstname} -------------- {self.created_at}------------ CV sent: {self.cv}"
