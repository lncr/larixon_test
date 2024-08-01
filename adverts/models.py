from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Advert(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='adverts', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='adverts', null=True)
