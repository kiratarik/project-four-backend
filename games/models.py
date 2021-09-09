from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    rules = models.TextField(max_length=5000)
    # liked_by = models.ManyToManyField(
    #     'jwt_auth.User',
    #     related_name='liked_characters',
    #     blank=True
    # )

    def __str__(self):
        return f'{self.name}'