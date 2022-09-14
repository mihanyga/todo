from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField("Имя проекта", max_length=64)
    link = models.URLField("Ссылка на репозиториий", max_length=255)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.CharField("Заметка", max_length=255)
    create_data = models.DateTimeField("Создана")
    update_data = models.DateTimeField("Обновлена")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField("Активно")