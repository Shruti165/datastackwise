# Generated by Django 5.1.3 on 2024-11-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.TextField()),
                ('benefits', models.TextField()),
                ('advantages', models.TextField()),
                ('disadvantages', models.TextField()),
                ('best_use_cases', models.TextField()),
                ('companies_using', models.TextField()),
                ('data_operations', models.TextField()),
                ('cost_analysis', models.TextField()),
                ('existing_teams_to_connect', models.TextField()),
            ],
        ),
    ]
