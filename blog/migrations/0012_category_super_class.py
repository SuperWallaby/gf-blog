# Generated by Django 3.0.7 on 2020-08-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='super_class',
            field=models.CharField(choices=[('BK', 'BOOKING'), ('TS', 'TIME_SAPCE'), ('TA', 'TEMPLATE_A')], default='BK', max_length=2),
        ),
    ]
