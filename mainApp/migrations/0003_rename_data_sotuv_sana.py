# Generated by Django 5.0.1 on 2024-07-11 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_sotuv_otish_alter_sotuv_tara'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sotuv',
            old_name='data',
            new_name='sana',
        ),
    ]
