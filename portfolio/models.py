from django.utils.timezone import now
from django.db import models
from cloudinary.models import CloudinaryField

CATEGORY_CHOICES = (
    ('website','Website'),
    ('webapp', 'Web-app'),
    ('uxui','UX/UI'), 
    ('other', 'Others')   
)

class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Info(models.Model):
    profile_pic = CloudinaryField("profile_pic", proxy="http://proxy.server:3128")
    name = models.CharField("Full name", max_length=60, default='Nattapol Boonyapornpong')
    nick_name = models.CharField("Nickname", max_length=20)
    description = models.CharField("description about yourself", max_length=600)
    email = models.EmailField("email", max_length=254)
    phone = models.CharField("phone", max_length=128, default='+66981322686')
    instagram = models.URLField('IG', max_length=200, default='https://instagram.com/jadenttp')
    github = models.URLField('Github', max_length=200, default='https://github.com/bleachjade')
    resume = models.URLField("Resume", max_length=200, default='https://drive.google.com/file/d/1nb04UNLb4J2hRhoOSojS7PW_846Bp02C/view?usp=sharing')

    def get_profile_image(self):
        return self.profile_pic

class Skill(models.Model):
    skill_image = CloudinaryField("Skill image", proxy="http://proxy.server:3128")
    skill_name = models.CharField('Skill name', max_length=50)

    def get_image(self):
        return self.skill_image

class Project(models.Model):
    project_image = CloudinaryField("Project image", proxy="http://proxy.server:3128")
    project_name = models.CharField('Project name', max_length=70)
    project_description = models.CharField("Project description", max_length=500)
    # project_category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='website')
    project_category = models.ManyToManyField(Category)
    project_date = models.DateField("Project Date", default=now)
    project_link = models.URLField('Project URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.project_image

class Contact(models.Model):
    from_email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)