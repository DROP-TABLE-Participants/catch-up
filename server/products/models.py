from uuid import uuid4

from django.db import models


from authentication.models import User


def upload_to(instance, filename):
    return '{filename}'.format(filename=str(uuid4()) + filename)


class Product(models.Model):
    name = models.CharField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    serialized_name = models.CharField()