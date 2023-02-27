from django.db import models

# Создаём модель новости
class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия новостей не должны повторяться
    )
    creationTime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name.title()}: {self.description[:50]}'

