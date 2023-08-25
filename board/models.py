from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    is_activated = models.BooleanField(
        default=True, db_index=True, verbose_name='Прошёл активацию?'
    )


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name="Текст отклика")
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name="Объявление", related_name='connect_post'
                             )
    author = models.OneToOneField('Author', on_delete=models.CASCADE, to_field='user', null=True, blank=True, )

    def get_absolute_url(self):
        return reverse('posts_url')


class Category(models.Model):
    category = models.CharField(max_length=64, verbose_name="Категория")

    def __str__(self):
        return self.category
