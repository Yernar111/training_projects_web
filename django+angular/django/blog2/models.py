# Та же модель что и в blog1.
from django.db import models
class ModelOne(models.Model):
    name = models.CharField(max_length=20, db_column="name")
    password = models.IntegerField(db_column="password")

    class Meta:
        db_table = "users1"
        managed = False

# Create your models here.