# Generated by Django 3.1.2 on 2021-04-09 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0013_auto_20210409_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='logs',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.siteuser'),
        ),
    ]