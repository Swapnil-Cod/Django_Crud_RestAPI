# Generated by Django 4.0.5 on 2022-08-31 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_id_employee_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]