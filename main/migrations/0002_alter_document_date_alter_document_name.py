# Generated by Django 4.1.5 on 2023-01-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата в документе'),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(choices=[('income', 'приход'), ('outcome', 'расход')], default='income', max_length=10),
        ),
    ]