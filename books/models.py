from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Available")
    borrower = models.ForeignKey('system_user.CustomUser',
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)
    return_date = models.DateTimeField(null=True, blank=True)


def __str__(self):
    return self.title

# Create your models here.
