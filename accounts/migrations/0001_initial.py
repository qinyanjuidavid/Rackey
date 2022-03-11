# Generated by Django 4.0.2 on 2022-03-11 19:41

from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='full name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('role', models.CharField(choices=[('Administrator', 'Administrator'), ('Customer', 'Customer'), ('Dealer', 'Dealer')], max_length=56, verbose_name='role')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=40, unique=True, verbose_name='county')),
            ],
            options={
                'verbose_name_plural': 'Counties',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='picture/%y/%m/%d', verbose_name='profile picture')),
                ('approve', models.BooleanField(default=True, verbose_name='approve')),
                ('protect_email', models.BooleanField(default=True, verbose_name='protect email')),
                ('derivery', models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=10, null=True, verbose_name='derivery')),
                ('level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Ameture', 'Ameture'), ('Pro', 'Pro')], max_length=14, null=True, verbose_name='delivery level')),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('estate', models.CharField(blank=True, max_length=106, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='farmers.productcategory')),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.counties')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResponseTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=15, unique=True, verbose_name='response time')),
            ],
            options={
                'verbose_name_plural': 'Response Time',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=157, verbose_name='item')),
                ('quantity', models.FloatField(default=0.0, help_text='Number of Kgs available')),
                ('image', models.ImageField(upload_to='products/%y%m/%d')),
                ('price', models.FloatField(verbose_name='price')),
                ('approve', models.BooleanField(default=True, verbose_name='approve')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('on_stock', models.BooleanField(default=True, verbose_name='on stock')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farmers.productcategory')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dealer')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='dealer',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.responsetime'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='picture/%y/%m/%d', verbose_name='profile picture')),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('estate', models.CharField(blank=True, max_length=106, null=True)),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.counties')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='picture/%y/%m/%d', verbose_name='profile picture')),
                ('job_id', models.CharField(blank=True, max_length=14, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
