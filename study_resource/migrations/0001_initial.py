# Generated by Django 3.1.3 on 2021-02-08 10:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('audio', models.FileField(blank=True, upload_to='resource/audios/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('ebook', models.FileField(blank=True, upload_to='resource/ebooks/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.FileField(blank=True, upload_to='resource/images/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StudyResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.FileField(blank=True, upload_to='cover_image/images/')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('study_level', models.CharField(max_length=500)),
                ('study_category', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('video', models.FileField(blank=True, upload_to='resource/videos/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceVideoConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.video')),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceLinkConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.link')),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceImageConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.image')),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceEbookConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.ebook')),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceContentConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.content')),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
            ],
        ),
        migrations.CreateModel(
            name='StudyResourceAudioConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.audio')),
                ('study_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_resource.studyresource')),
            ],
        ),
        migrations.AddField(
            model_name='studyresource',
            name='audios',
            field=models.ManyToManyField(through='study_resource.StudyResourceAudioConnector', to='study_resource.Audio'),
        ),
        migrations.AddField(
            model_name='studyresource',
            name='contents',
            field=models.ManyToManyField(through='study_resource.StudyResourceContentConnector', to='study_resource.Content'),
        ),
        migrations.AddField(
            model_name='studyresource',
            name='ebooks',
            field=models.ManyToManyField(through='study_resource.StudyResourceEbookConnector', to='study_resource.Ebook'),
        ),
        migrations.AddField(
            model_name='studyresource',
            name='images',
            field=models.ManyToManyField(through='study_resource.StudyResourceImageConnector', to='study_resource.Image'),
        ),
        migrations.AddField(
            model_name='studyresource',
            name='links',
            field=models.ManyToManyField(through='study_resource.StudyResourceLinkConnector', to='study_resource.Link'),
        ),
        migrations.AddField(
            model_name='studyresource',
            name='videos',
            field=models.ManyToManyField(through='study_resource.StudyResourceVideoConnector', to='study_resource.Video'),
        ),
    ]
