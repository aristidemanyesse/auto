# Generated by Django 3.2.9 on 2021-11-15 18:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('acompte_initial', models.IntegerField(blank=True, default=0, null=True)),
                ('dette_initial', models.IntegerField(blank=True, default=0, null=True)),
                ('seuil_credit', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeClient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('etiquette', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]