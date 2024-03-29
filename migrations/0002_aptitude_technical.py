# Generated by Django 2.0.2 on 2018-03-17 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fuzzy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptitude', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Semester')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Semester')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Student')),
            ],
        ),
    ]
