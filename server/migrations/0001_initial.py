# Generated by Django 3.1.7 on 2021-03-02 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.CharField(max_length=8, verbose_name='Student ID')),
                ('dob', models.CharField(max_length=10, verbose_name='Date of birth')),
                ('gender', models.CharField(max_length=8, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('vnu_email', models.CharField(max_length=50, verbose_name='VNU email')),
                ('other_email', models.CharField(max_length=50, verbose_name='Other email')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='server.student')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=50, verbose_name='Contact name')),
                ('contact_addr', models.CharField(max_length=100, verbose_name='Contact address')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='server.student', verbose_name='Student')),
            ],
        ),
    ]
