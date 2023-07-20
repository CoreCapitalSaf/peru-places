import xlrd
import requests

from django.core.management.base import BaseCommand, CommandError

from places.loader import Loader


class Command(BaseCommand):
    """
    Supported languages: EN, ES (--language)
    """

    help = 'Supported languages: EN, ES (--language)'

    def add_arguments(self, parser):
        """
        Function to add arguments

        :param parser: CommandParser for the command
        """

        parser.add_argument(
            '--from_url',
            action='store_true',
            help='Url where to download the Peru xlsx data',
        )
        parser.add_argument(
            '--language', type=str, help='By default it receives EN')

    def handle(self, *args, **options):
        """
        Function to handle the command

        :param args: args for the command
        :param options: key word options
        """

        try:
            loader = Loader()
            loader.load_peru(from_url=options.get('from_url'))
            loader.load_countries(language=options.get('language'))
            loader.load_cities()
        except (requests.HTTPError, requests.ConnectionError, xlrd.XLRDError) as err:
            raise CommandError('Unable te get the places: "%s"' % err)
        self.stdout.write(self.style.SUCCESS('Places saved successfully'));