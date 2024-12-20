# Generated by Django 5.0.1 on 2024-06-12 10:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xarajatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umumiy_xarajat', models.FloatField()),
                ('sabab', models.CharField(blank=True, max_length=255, null=True)),
                ('sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Xaridor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('familya', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=100)),
                ('tel_1', models.CharField(max_length=13)),
                ('tel_2', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sotuv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meva_turi', models.CharField(choices=[('SUPER', 'SUPER'), ('LOLA 1', 'LOLA 1'), ('LOALA 2', 'LOLA 2')], max_length=20)),
                ('bog', models.CharField(choices=[("Katta bog'", "Katta bog'"), ("Yangi bog'", "Yangi bog'"), ('Burchak', 'Burchak'), ('Ishxona', 'Ishxona')], max_length=20)),
                ('quti_turi', models.CharField(choices=[('karzinka', 'karzinka'), ('yashik', 'yashik'), ('karobka', 'karobka')], max_length=20)),
                ('quti_soni', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('tara', models.FloatField()),
                ('otish', models.FloatField()),
                ('data', models.DateField()),
                ('xaridor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.xaridor')),
            ],
        ),
    ]
