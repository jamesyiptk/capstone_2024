# Generated by Django 5.1.3 on 2024-11-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_analytics', '0007_remove_resourcerequest_training_an_start_t_80b9a6_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10)),
                ('average_participants', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-average_participants'],
            },
        ),
        migrations.CreateModel(
            name='IndustryParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=255)),
                ('average_participants', models.FloatField()),
                ('average_experience', models.FloatField(null=True)),
                ('total_experience', models.FloatField(null=True)),
                ('entry_count', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-average_participants'],
            },
        ),
        migrations.CreateModel(
            name='MonthlyTopicTrend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('month', models.IntegerField()),
                ('request_count', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-request_count'],
                'indexes': [models.Index(fields=['topic'], name='training_an_topic_0c0e7e_idx'), models.Index(fields=['month'], name='training_an_month_8f6e6c_idx'), models.Index(fields=['request_count'], name='training_an_request_b2685e_idx')],
                'unique_together': {('topic', 'month')},
            },
        ),
        migrations.CreateModel(
            name='RegionalParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
                ('total_participants', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-total_participants'],
                'indexes': [models.Index(fields=['state'], name='training_an_state_40548d_idx'), models.Index(fields=['county'], name='training_an_county_b9fabf_idx')],
            },
        ),
        migrations.CreateModel(
            name='SeasonalTopicTrend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('season', models.CharField(choices=[('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], max_length=10)),
                ('request_count', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-request_count'],
                'indexes': [models.Index(fields=['topic'], name='training_an_topic_e688b2_idx'), models.Index(fields=['season'], name='training_an_season_1aa18a_idx'), models.Index(fields=['request_count'], name='training_an_request_664ca9_idx')],
                'unique_together': {('topic', 'season')},
            },
        ),
        migrations.CreateModel(
            name='TimeSlotAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=50)),
                ('average_attendance', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-average_attendance'],
                'indexes': [models.Index(fields=['time_slot'], name='training_an_time_sl_62994b_idx')],
            },
        ),
        migrations.CreateModel(
            name='TopicFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('frequency', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Topic frequencies',
                'ordering': ['-frequency'],
                'indexes': [models.Index(fields=['topic'], name='training_an_topic_c9b911_idx'), models.Index(fields=['frequency'], name='training_an_frequen_087179_idx')],
            },
        ),
    ]