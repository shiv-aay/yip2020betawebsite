# Generated by Django 2.2.14 on 2020-09-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200911_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s3_class',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s3_dob',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]