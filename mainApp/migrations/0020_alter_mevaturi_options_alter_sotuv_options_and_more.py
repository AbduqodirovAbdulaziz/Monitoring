# Generated by Django 5.0.1 on 2024-10-28 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_alter_xarajatlar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mevaturi',
            options={'verbose_name_plural': 'Meva turlari'},
        ),
        migrations.AlterModelOptions(
            name='sotuv',
            options={'verbose_name_plural': 'Sotuvlar'},
        ),
        migrations.AlterModelOptions(
            name='xarajatlar',
            options={'verbose_name_plural': 'Xarajatlar'},
        ),
        migrations.AlterModelOptions(
            name='xaridor',
            options={'verbose_name_plural': 'Xaridorlar'},
        ),
    ]