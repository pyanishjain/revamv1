# Generated by Django 3.0.2 on 2020-03-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]