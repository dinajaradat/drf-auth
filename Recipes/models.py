from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255,null=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe_box=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name