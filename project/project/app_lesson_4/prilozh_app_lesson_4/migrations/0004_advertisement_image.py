# Generated by Django 4.2.5 on 2023-10-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prilozh_app_lesson_4', '0003_advertisement_user_alter_advertisement_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='app_lesson_4/', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]
