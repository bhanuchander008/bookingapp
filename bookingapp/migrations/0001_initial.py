# Generated by Django 3.0.5 on 2021-03-24 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=250)),
                ('lastName', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('profile_for', models.CharField(choices=[('M', 'myself'), ('b', 'brother'), ('S', 'Son'), ('SS', 'Sister'), ('F', 'Friend'), ('R', 'Relative')], max_length=12)),
            ],
        ),
    ]