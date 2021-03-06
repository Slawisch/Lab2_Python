# Generated by Django 3.1.7 on 2021-04-28 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text='Максимум 250 символів', max_length=250, verbose_name='Категорія')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категорія для публікації',
                'verbose_name_plural': 'Категорії для публікацій',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_page', models.BooleanField()),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab2.category')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab2.image')),
            ],
        ),
    ]
