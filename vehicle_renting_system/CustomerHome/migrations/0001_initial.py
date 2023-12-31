# Generated by Django 4.2.3 on 2023-11-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_firstname', models.CharField(max_length=60)),
                ('customer_lastname', models.CharField(max_length=60)),
                ('customer_address', models.CharField(max_length=600)),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_password', models.CharField(max_length=32)),
                ('customer_dob', models.DateField()),
                ('customer_mobileno', models.CharField(max_length=10)),
                ('customer_gender', models.CharField(max_length=15)),
                ('customer_license', models.ImageField(upload_to='img/Customer_License/')),
                ('customer_city', models.CharField(max_length=30)),
                ('customer_state', models.CharField(max_length=30)),
                ('customer_country', models.CharField(max_length=30)),
                ('customer_pincode', models.IntegerField()),
            ],
        ),
    ]
