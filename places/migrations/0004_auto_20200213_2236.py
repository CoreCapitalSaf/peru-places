# Generated by Django 3.0.2 on 2020-02-13 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20200213_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name': 'county', 'verbose_name_plural': 'counties'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'district', 'verbose_name_plural': 'districts'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='province',
        ),
        migrations.RemoveField(
            model_name='address',
            name='region',
        ),
        migrations.RemoveField(
            model_name='city',
            name='region',
        ),
        migrations.RemoveField(
            model_name='district',
            name='province',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.City', verbose_name='city'),
        ),
        migrations.AddField(
            model_name='address',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.County', verbose_name='county'),
        ),
        migrations.AddField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=10, verbose_name='number'),
        ),
        migrations.AddField(
            model_name='address',
            name='second_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='second number'),
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(blank=True, max_length=6, verbose_name='zip code'),
        ),
        migrations.AddField(
            model_name='city',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.County', verbose_name='county'),
        ),
        migrations.AddField(
            model_name='district',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.City', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='detail',
            field=models.CharField(blank=True, max_length=200, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]