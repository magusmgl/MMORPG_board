# Generated by Django 3.2.15 on 2022-10-19 22:19

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', default='', help_text='enter title of advertisement', max_length=200, verbose_name='Advertisement  title')),
                ('date', models.DateField(auto_now_add=True, db_column='date')),
                ('content_upload', ckeditor_uploader.fields.RichTextUploadingField(blank=True, db_column='content_upload', null=True)),
                ('author', models.ForeignKey(db_column='ad author', help_text='choose author of advertisement', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Advertisement author')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(db_column='response_text', help_text='enter text of response', max_length=200, verbose_name='Response text')),
                ('advertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='board.advertisement')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
