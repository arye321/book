from django.db import models

# Create your models here.

class Skill(models.Model):
    skill = models.CharField(max_length=40)
    def __str__(self):
        return self.skill
class Candidate(models.Model):
    
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
class Job(models.Model):
    title = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return self.title