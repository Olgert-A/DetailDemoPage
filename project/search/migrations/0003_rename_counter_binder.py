# Generated by Django 4.0.5 on 2022-09-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_remove_detail_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Counter',
            new_name='Binder',
        ),
    ]