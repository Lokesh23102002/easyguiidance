<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-02-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_alter_calc_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
=======
# Generated by Django 4.0.1 on 2022-02-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_alter_calc_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
>>>>>>> feff908ca3cc4f9fc888c5f3fcf21edaf7ac79b9
