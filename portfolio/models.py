from django.db import models


class Info(models.Model):
    profile_pic = models.ImageField("Profile picture", upload_to='profile_pics/', height_field=None, width_field=None, max_length=None)
    name = models.CharField("Full name", max_length=50, default='Jade')
    nick_name = models.CharField("Nickname", max_length=20)
    description = models.CharField("description about yourself", max_length=300)
    email = models.EmailField("email", max_length=254)
    resume = models.FileField("resume", upload_to='resumes/', max_length=100)