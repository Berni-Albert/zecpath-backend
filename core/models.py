from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    skills = models.TextField()

    def __str__(self):
        return self.user.username


class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Application(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    status = models.CharField(max_length=20, default="Pending")

    applied_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.candidate} - {self.job}"