# Generated by Django 4.0.1 on 2022-03-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
