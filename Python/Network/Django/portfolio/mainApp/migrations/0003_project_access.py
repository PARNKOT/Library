# Generated by Django 4.1.7 on 2023-03-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_last_updated_project_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=20),
            preserve_default=False,
        ),
    ]