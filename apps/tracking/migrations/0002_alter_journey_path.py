# Generated by Django 4.1.5 on 2023-01-16 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='path',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tracking.path'),
            preserve_default=False,
        ),
    ]