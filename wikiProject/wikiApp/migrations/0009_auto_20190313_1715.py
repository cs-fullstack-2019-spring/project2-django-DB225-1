# Generated by Django 2.0.6 on 2019-03-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0008_auto_20190313_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]