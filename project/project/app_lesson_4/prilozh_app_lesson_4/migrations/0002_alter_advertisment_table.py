from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prilozh_app_lesson_4', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]