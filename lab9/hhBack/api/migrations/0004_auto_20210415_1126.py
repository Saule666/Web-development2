# Generated by Django 2.1.5 on 2021-04-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210414_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]