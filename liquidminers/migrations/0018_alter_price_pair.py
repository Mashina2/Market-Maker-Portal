# Generated by Django 3.2.9 on 2022-01-31 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liquidminers', '0017_auto_20220128_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='pair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='liquidminers.pair'),
        ),
    ]