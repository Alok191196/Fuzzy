# Generated by Django 2.0.2 on 2018-03-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fuzzy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_s', models.IntegerField()),
                ('external_s', models.IntegerField()),
                ('attendance_s', models.IntegerField()),
                ('res_s', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal', models.IntegerField()),
                ('external', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Branch')),
                ('sem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Semester')),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='sem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Semester'),
        ),
        migrations.AddField(
            model_name='marks',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subj_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Subjects'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='sem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Semester'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fuzzy.Student'),
        ),
    ]