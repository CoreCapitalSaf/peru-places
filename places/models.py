from django.db import models


class Address(models.Model):
    """
    Class for Adresses

    :cvar country: ForeignKey to Country.
    :cvar county: ForeignKey to County.
    :cvar city: ForeignKey to City.
    :cvar district: ForeignKey to District.
    :cvar detail: CharField with the address detail.
    """

    country = models.ForeignKey(
        'places.Country', verbose_name='country',
        on_delete=models.CASCADE, null=True, blank=True)
    county = models.ForeignKey(
        'places.County', verbose_name='county',
        on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(
        'places.City', verbose_name='city',
        on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(
        'places.District', verbose_name='district', on_delete=models.CASCADE,
        null=True, blank=True)
    detail = models.CharField('address', max_length=200, blank=True)
    zip_code = models.CharField('zip code', max_length=6, blank=True)
    number = models.CharField('number', max_length=10, blank=True)
    second_number = models.CharField('second number', max_length=10, blank=True)

    def __str__(self):
        return self.get_full_address()

    def get_address(self):
        """
        Function in charge of composing the house complete address

        :return: String with the house number included
        """

        address = (self.detail, self.number, self.second_number)

        return ' '.join(filter(None, address))

    def get_full_address(self):
        """
        Returns complete address(detail, district, city, country).
        """

        return (
            f"{self.get_address()} {self.district} {self.city}, {self.county}, "
            f"{self.country}")

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'


class Country(models.Model):
    """
    Class for Countries

    :cvar name: CharField for Country name.
    :cvar code: CharField for Country code.
    """

    name = models.CharField('name', max_length=50)
    code = models.CharField('code', max_length=10, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class County(models.Model):
    """
    Class for Counties

    :cvar name: CharField for County name.
    :cvar country: ForeignKey to Country wich belongs to.
    :cvar code: CharField for County code.
    """

    name = models.CharField('name', max_length=50)
    country = models.ForeignKey(
        'places.Country', verbose_name='country', on_delete=models.CASCADE, null=True)
    code = models.CharField('code', max_length=10, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'county'
        verbose_name_plural = 'counties'

    @staticmethod
    def autocomplete_search_fields():
        return 'name',


class City(models.Model):
    """
    Class para las Provincias.

    :cvar name: CharField for City name.
    :cvar county: ForeignKey to County wich belongs to.
    :cvar code: CharField for City code.
    """

    name = models.CharField('name', max_length=50)
    county = models.ForeignKey(
        'places.County', verbose_name='county', on_delete=models.CASCADE, null=True)
    code = models.CharField('code', max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class District(models.Model):
    """
    Class for districts

    :cvar name: CharField for the district name.
    :cvar city: ForeignKey of City wich it belongs to.
    :cvar code: CharField for the district code.
    :cvar ubigeo: CharField for ubigeo code.
    """

    name = models.CharField('name', max_length=50)
    city = models.ForeignKey(
        'places.City', verbose_name='city',
        on_delete=models.CASCADE, null=True)
    code = models.CharField('code', max_length=5, blank=True)
    ubigeo = models.CharField('ubigeo', max_length=6, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'district'
        verbose_name_plural = 'districts'
