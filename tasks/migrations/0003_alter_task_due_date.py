# Generated by Django 4.2.2 on 2023-06-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_description_alter_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
