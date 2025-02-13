from django.db import models

class Profile(models.Model):
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('red', 'Red')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name
    
class Links(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='link')

    def __str__(self):
        return f"{self.text} | {self.url}"
