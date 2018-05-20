# Generated by Django 2.0.4 on 2018-05-20 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20180520_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocategory',
            name='team',
            field=models.ForeignKey(help_text='The team responsible for this info category.', on_delete=django.db.models.deletion.PROTECT, related_name='info_categories', to='teams.Team'),
        ),
    ]
