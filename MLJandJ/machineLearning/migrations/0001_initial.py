# Generated by Django 4.1.4 on 2022-12-21 23:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mpg', models.FloatField()),
                ('horsepower', models.FloatField()),
            ],
        ),
    ]
