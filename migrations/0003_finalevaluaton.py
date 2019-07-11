# Generated by Django 2.0.2 on 2018-03-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fuzzy', '0002_aptitude_technical'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalEvaluaton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal', models.TextField()),
                ('external', models.TextField()),
                ('attendance', models.TextField()),
                ('output', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
