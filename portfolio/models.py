from django.utils.timezone import now
from django.db import models
from cloudinary.models import CloudinaryField


class Info(models.Model):
    profile_pic = CloudinaryField("profile_pic", proxy="http://proxy.server:3128")
    name = models.CharField("Full name", max_length=50, default='Jade')
    nick_name = models.CharField("Nickname", max_length=20)
    description = models.CharField("description about yourself", max_length=300)
    email = models.EmailField("email", max_length=254)
    instagram = models.URLField('IG', max_length=200, default='https://instagram.com/jadenttp')
    github = models.URLField('Github', max_length=200, default='https://github.com/bleachjade')

    def get_profile_image(self):
        return self.profile_pic

class Skill(models.Model):
    skill_image = CloudinaryField("skill_img", proxy="http://proxy.server:3128")
    skill_name = models.CharField('Skill name', max_length=50)

    def get_image(self):
        return self.skill_image

class Work(models.Model):
    project_image = CloudinaryField("project_img", proxy="http://proxy.server:3128")
    project_name = models.CharField('Project name', max_length=50)
    project_description = models.CharField("Project description", max_length=200)
    project_date = models.DateField("Project Date", default=now)
    project_link = models.URLField('Project URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.project_image

class InternshipWork(models.Model):
    project_image = CloudinaryField("project_img", proxy="http://proxy.server:3128")
    project_name = models.CharField('Project name', max_length=50)
    project_description = models.CharField("Project description", max_length=200)
    project_date = models.DateField("Project Date", default=now)
    project_link = models.URLField('Project URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.project_image

class FreelanceWork(models.Model):
    project_image = CloudinaryField("project_img", proxy="http://proxy.server:3128")
    project_name = models.CharField('Project name', max_length=50)
    project_description = models.CharField("Project description", max_length=200)
    project_date = models.DateField("Project Date", default=now)
    project_link = models.URLField('Project URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.project_image

class Activity(models.Model):
    activity_image = CloudinaryField("activity_img", proxy="http://proxy.server:3128")
    activity_name = models.CharField('Activity name', max_length=50)
    activity_description = models.CharField("Activity description", max_length=200)
    activity_date = models.DateField("Activity Date", default=now)
    activity_link = models.URLField('Activity URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.activity_image

class Contact(models.Model):
    from_email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)