# Generated by Django 2.0 on 2019-01-04 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment', to='blog.Blog'),
        ),
    ]
