# Generated by Django 5.0.1 on 2024-10-28 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_alter_xarajatlar_umumiy_xarajat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sotuv',
            name='quti_ogirligi',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
    ]
