# Generated by Django 5.1.6 on 2025-02-26 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0011_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='category',
            field=models.ForeignKey(blank=True, default=('unconverted', 'Unconverted'), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_leads', to='lead.category'),
        ),
    ]
