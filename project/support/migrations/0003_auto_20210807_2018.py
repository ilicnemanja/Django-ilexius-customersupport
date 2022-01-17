# Generated by Django 3.2.6 on 2021-08-07 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='customer_support',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='support.customersupport'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.user'),
        ),
    ]
