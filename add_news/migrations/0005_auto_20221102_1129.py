# Generated by Django 2.2 on 2022-11-02 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_news', '0004_auto_20221101_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='add_date',
        ),
        migrations.AlterField(
            model_name='articles',
            name='date_add',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='update_date',
            field=models.DateTimeField(verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_news', to='add_news.Articles', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text_comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
    ]