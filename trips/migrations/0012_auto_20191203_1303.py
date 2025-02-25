# Generated by Django 2.2.5 on 2019-12-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_auto_20191203_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the service type', max_length=300, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.ServiceType'),
        ),
    ]
