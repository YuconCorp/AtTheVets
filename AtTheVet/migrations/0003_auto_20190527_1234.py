# Generated by Django 2.1.7 on 2019-05-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtTheVet', '0002_auto_20190522_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaratie',
            name='declaratie_id',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='factuur',
            name='factuur_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
