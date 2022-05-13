# Generated by Django 4.0.4 on 2022-05-11 06:56

from django.db import migrations, models
import django.db.models.deletion
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=128)),
                ('priority', models.PositiveIntegerField()),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='categories/icons')),
                ('featured_image', versatileimagefield.fields.VersatileImageField(upload_to='categories/featured_images')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('-priority',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(max_length=128)),
                ('icon', versatileimagefield.fields.VersatileImageField(upload_to='services/icons')),
                ('featured_image', versatileimagefield.fields.VersatileImageField(upload_to='services/featured_images')),
                ('description', models.TextField()),
                ('cost_type', models.CharField(choices=[('HOURLY', 'HOURLY'), ('PER_DAY', 'PER_DAY'), ('PER_WORK', 'PER_WORK')], max_length=128)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=128)),
                ('category', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.PROTECT, to='services.category')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
