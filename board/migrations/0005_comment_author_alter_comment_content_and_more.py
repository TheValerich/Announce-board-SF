# Generated by Django 4.2.4 on 2023-08-17 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.author', to_field='user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Текст отклика'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connect_post', to='board.post', verbose_name='Объявление'),
        ),
    ]
