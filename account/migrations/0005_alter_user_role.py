# Generated by Django 4.2.1 on 2024-08-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('agent', 'Agent'), ('manager', 'Manager'), ('user', 'User')], default='user', max_length=20),
        ),
    ]
