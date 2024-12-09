# Generated by Django 5.1.3 on 2024-12-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_network_app', '0002_company_company_description_company_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
