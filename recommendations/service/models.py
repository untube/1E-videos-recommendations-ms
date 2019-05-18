from django.db import models

# Create your models here.
class UserPreferences(models.Model):
    id_user = models.IntegerField(null=False)
    id_category = models.IntegerField(null=False)
    counter = models.IntegerField(default=0)
class VideoStatistics(models.Model):
    id_video = models.IntegerField(null=False)
    id_category = models.IntegerField(null=False)
    calification = models.IntegerField(default=0)
    num_views = models.IntegerField(default=1)