# Generated by Django 5.0.6 on 2024-11-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('price_band', models.CharField(max_length=50)),
                ('open_date', models.DateField()),
                ('close_date', models.DateField()),
                ('issue_size', models.IntegerField()),
                ('issue_type', models.CharField(max_length=50)),
                ('listing_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('ipo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('listing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_market_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_return', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rhp_pdf', models.FileField(upload_to='pdfs/')),
                ('drhp_pdf', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
