# Generated by Django 3.0.2 on 2020-02-03 16:25

from django.db import migrations

from places.loader import Loader

def load_data(apps, schema_editor):
    """
    Function that loads the data
    """
    loader = Loader()
    loader.load()

def reverse_func(apps, schema_editor):
    """
    Fucntion that reverse load_data function deleting Country instances.
    It also will delete regions, provinces and districts.
    """
    Country = apps.get_model("places", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_func),
    ]
