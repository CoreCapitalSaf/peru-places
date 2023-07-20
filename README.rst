===========
Places
===========

Places is a Django app to get places from the world. It gets all counties,
cities and districts from Perú and saves them. For the rest of the world,
only countries and counties are saved.

Places for Perú is automatically loaded in mgirations. The rest of the places
is loaded through the command `python manage.py load_places`

Quick start
-----------

1. Add "places" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'places',
    ]



2. Run `python manage.py migrate` to create the places models.



3. Run the the following command to get and save the places.
IMPORTANT: this will load all the places, so it will take about 1 hour::

	$ ./manage.py load_places

