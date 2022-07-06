from django.db import models
class Book(models.Model):
    STATUS = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('unavailable', 'Unavailable')  
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS)
    subject_area = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'books' 

    def __str__(self):
        return self.title
