# Generated by Django 2.0 on 2019-01-04 10:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190104_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('read_detail_num', models.IntegerField(default=0)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='read_detail_num', to='blog.Blog')),
            ],
        ),
    ]
