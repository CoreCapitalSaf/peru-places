from django.contrib import admin

from places.models import Country, County, City, District


admin.site.register(Country)
admin.site.register(County)
admin.site.register(City)
admin.site.register(District)
