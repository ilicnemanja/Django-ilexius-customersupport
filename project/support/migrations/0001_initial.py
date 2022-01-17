# Generated by Django 3.2.6 on 2021-08-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.CharField(max_length=32)),
                ('subject', models.CharField(max_length=50)),
                ('issue_description', models.TextField()),
                ('date_time', models.CharField(blank=True, max_length=20)),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]