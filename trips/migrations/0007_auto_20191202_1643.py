# Generated by Django 2.2.5 on 2019-12-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20191202_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.IntegerField(choices=[(1, 'Hotel'), (2, 'Accommodation'), (3, 'Transportation')], help_text='The type of service (Hotel, Accomodation or Transportation)'),
        ),
    ]
