# Generated by Django 3.2.5 on 2021-07-29 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Описание')),
                ('parent_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('tree_id', models.PositiveIntegerField(blank=True, db_index=True)),
                ('lft', models.PositiveIntegerField(blank=True, db_index=True)),
                ('rgt', models.PositiveIntegerField(blank=True, db_index=True)),
                ('depth', models.PositiveIntegerField(blank=True, db_index=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.article')),
            ],
            options={
                'verbose_name': 'Комментарий',
            },
        ),
    ]
