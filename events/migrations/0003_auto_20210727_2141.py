# Generated by Django 3.2.5 on 2021-07-27 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_alter_event_participants_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=90, verbose_name='Свойство')),
            ],
            options={
                'verbose_name': 'Свойство события',
                'verbose_name_plural': 'Свойства события',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants_number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество участников'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(default=0)),
                ('text', models.TextField(default='', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='events.event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв на событие',
                'verbose_name_plural': 'Отзывы на события',
            },
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolls', to='events.event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolls', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запись на событие',
                'verbose_name_plural': 'Записи на событие',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='features',
            field=models.ManyToManyField(blank=True, to='events.Feature'),
        ),
    ]
