from django.db import models


class Book(models.Model):
    autho = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='static')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
