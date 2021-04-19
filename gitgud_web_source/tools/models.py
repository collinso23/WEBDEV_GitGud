from django.db import models

# Create your models here.
class ToolsModel(models.Model):
    toolname = models.CharField(max_length=200)
    parameters = models.CharField(max_length=200)
