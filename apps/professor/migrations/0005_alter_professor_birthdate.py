# Generated by Django 3.2.6 on 2021-08-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0004_professor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
