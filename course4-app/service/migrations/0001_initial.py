# Generated by Django 3.2.16 on 2022-11-18 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(choices=[('full', 'Full'), ('student', 'Student'), ('discount', 'Discount')], max_length=10)),
                ('discount_percent', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('full_price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.plan')),
            ],
        ),
    ]
