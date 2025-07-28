from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=255)
    music_file = models.FileField(upload_to='music/')
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)  
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name
