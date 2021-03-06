# Generated by Django 3.1.7 on 2021-03-14 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('answer_a', models.CharField(default='None', max_length=500)),
                ('answer_b', models.CharField(default='None', max_length=500)),
                ('answer_c', models.CharField(default='None', max_length=500)),
                ('answer_d', models.CharField(default='None', max_length=500)),
                ('real_answer', models.CharField(default='None', max_length=500)),
                ('category', models.CharField(default='general', max_length=500)),
                ('level', models.CharField(default='simple', max_length=500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
