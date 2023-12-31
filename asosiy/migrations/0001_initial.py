# Generated by Django 4.2 on 2023-07-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=75)),
                ('sana', models.DateField()),
                ('rasm', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=45)),
                ('tugilgan_yil', models.DateField()),
                ('davlat', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=65)),
                ('janr', models.CharField(max_length=60)),
                ('davomiylik', models.DurationField(null=True)),
                ('fayl', models.TextField(null=True)),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.qoshiqchi'),
        ),
    ]
