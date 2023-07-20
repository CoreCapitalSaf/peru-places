import os

import xlrd
import requests

import places
from places.constants import COUNTRIES, DEFAULT_LANGUAGE, COUNTRIES_ES
from places.models import Country, County, City, District


class Loader:
    """
    Class to import peru places
    """

    help = 'Load regions, provinces and districts'
    url = ('http://webinei.inei.gob.pe:8080/sisconcode/web/ubigeo/'
           'listaBusquedaUbigeoPorUbicacionGeograficaXls/5/1/1/null/null/null')

    def load(self):
        """
        Function that will pass because previous migration use this function
        """
        pass

    def load_peru(self, from_url=False):
        """
        Function that load places only for Perú
        """

        state_col = 1
        state_name = 'DEPARTAMENTO'
        city_col = 4
        county_col = 5
        if from_url:
            response = requests.get(self.url)
            book = xlrd.open_workbook(file_contents=response.content)
        else:
            book = xlrd.open_workbook(
                os.path.join(places.__path__[0], 'static', 'rptUbigeo.xls'))
        sh = book.sheet_by_index(0)
        country, _ = Country.objects.get_or_create(name='Perú', defaults=dict(
            code='PE'))
        for rx in range(sh.nrows):
            if sh.cell_value(rx, state_col) == state_name:
                continue
            if sh.cell_value(rx, state_col).strip() != '':
                state_list = sh.cell_value(rx, state_col).split(' ')
                state, _ = County.objects.get_or_create(
                    code=state_list[0],
                    name=' '.join(state_list[1:]).strip(),
                    defaults={'country': country},
                )
            if sh.cell_value(rx, city_col).strip() != '':
                city_list = sh.cell_value(rx, city_col).split(' ')
                city, _ = City.objects.get_or_create(
                    code=city_list[0],
                    county=state,
                    name=" ".join(city_list[1:]).strip()
                )
            if sh.cell_value(rx, county_col).strip() != '':
                county_list = sh.cell_value(rx, county_col).split(' ')
                county, _ = District.objects.get_or_create(
                    code=county_list[0],
                    city=city,
                    name=" ".join(county_list[1:]).strip()
                )

    def load_countries(self, language='EN'):
        """
        Function that load countries
        """

        if language == DEFAULT_LANGUAGE:
            countries = COUNTRIES
        elif language == 'ES':
            countries = COUNTRIES_ES
        for code, name in countries.items():
            Country.objects.update_or_create(code=code, name=name)

    def load_cities(self):
        """
        Function that load countries and cities of the provided excel
        """

        wr_code_col = 0
        wr_city_col = 1
        wr_country_col = 8
        book = xlrd.open_workbook(os.path.join(
            places.__path__[0], 'static', 'cities1000.xlsx'))
        sh = book.sheet_by_index(0)
        for rx in range(sh.nrows):
            code = str(sh.cell_value(rx, wr_code_col))[:10]
            city = str(sh.cell_value(rx, wr_city_col))[:50]
            country_code = str(sh.cell_value(rx, wr_country_col))[:10]
            if country_code != 'PE':
                country, _ = Country.objects.get_or_create(
                    code=country_code, defaults={'name': country_code})
                state, _ = County.objects.get_or_create(
                    code=code,
                    name=city,
                    defaults={'country': country},
                )