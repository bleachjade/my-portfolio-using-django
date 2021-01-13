from django.db import models


class Info(models.Model):
    profile_pic = models.ImageField("Profile picture", upload_to='upload/', height_field=None, width_field=None, max_length=None)
    name = models.CharField("Full name", max_length=50, default='Jade')
    nick_name = models.CharField("Nickname", max_length=20)
    description = models.CharField("description about yourself", max_length=300)
    email = models.EmailField("email", max_length=254)
    resume = models.FileField("resume", upload_to='resumes/', max_length=100)

class Work(models.Model):
    project_image = models.ImageField('Project image', upload_to='upload/', height_field=None, width_field=None, max_length=None)
    project_name = models.CharField('Project name', max_length=50)
    project_description = models.CharField("Project description", max_length=200)
    github_project = models.URLField('Github URL', max_length=128, default='https://github.com/bleachjade')

    def get_image(self):
        return self.project_image