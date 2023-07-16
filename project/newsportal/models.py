from django.db import models


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()
    date_on = models.DateField()

    def __str__(self):
        return f'{self.name.title()}: {self.text} {self.date_on}'

