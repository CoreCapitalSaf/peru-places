# Generated by Django 3.0.2 on 2020-01-30 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=5, null=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('code', models.CharField(blank=True, max_length=5, null=True, verbose_name='code')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=5, null=True, verbose_name='code')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'Province',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('code', models.CharField(blank=True, max_length=5, null=True, verbose_name='code')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Province', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'District',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=200, verbose_name='address')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Country', verbose_name='country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.District', verbose_name='district')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Province', verbose_name='province')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'Address',
            },
        ),
    ]
