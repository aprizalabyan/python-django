from django.db import models
from db_connection import db
from bson import ObjectId

# Create your models here.
user_collection = db["user"]


class User(models.Model):
    # _id = models.AutoField(primary_key=True)
    _id = ObjectId()
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
