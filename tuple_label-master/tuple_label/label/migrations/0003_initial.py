# Generated by Django 3.2.3 on 2021-06-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('label', '0002_auto_20210601_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('Belong', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'lable_admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('project_id', models.IntegerField()),
                ('annotations', models.CharField(default='[[]]', max_length=2048)),
                ('predications', models.TextField(default='[[]]')),
                ('is_checked', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'label_document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'label_project',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='label.project')),
            ],
            options={
                'db_table': 'lable_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('shortcut', models.CharField(max_length=8)),
                ('background_color', models.CharField(max_length=8)),
                ('text_color', models.CharField(max_length=8)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('project_id', models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, related_name='project_label', to='label.project')),
            ],
            options={
                'db_table': 'label_label',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Admin_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_user_id', models.IntegerField()),
                ('admin_id', models.ForeignKey(db_column='admin_id', on_delete=django.db.models.deletion.CASCADE, to='label.admin')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='label.user')),
            ],
            options={
                'db_table': 'lable_adminUser',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='admin',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='label.project'),
        ),
    ]
