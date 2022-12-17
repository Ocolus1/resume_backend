from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class ResumeProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user',
                           related_name='to_user', db_index=True)
    profile_pic = models.ImageField()
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    profile = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.first_name


class EmploymentHistory(models.Model):
    role = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    start_date = models.CharField(max_length=255, blank=True)
    end_date = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    employment_resume = models.ForeignKey(ResumeProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.role


class Education(models.Model):
    school = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    start_date = models.CharField(max_length=255, blank=True)
    end_date = models.CharField(max_length=255, blank=True)
    education_resume = models.ForeignKey(ResumeProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.school


class Website(models.Model):
    label = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    website_resume = models.ForeignKey(ResumeProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.label


class Skills(models.Model):
    label = models.CharField(max_length=255, blank=True)
    skills_resume = models.ForeignKey(ResumeProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

