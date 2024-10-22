import csv
from django.core.management.base import BaseCommand
from main.models import Publication

class Command(BaseCommand):
    help = 'Export publications to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The CSV file to export to')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'name',
                'publication_number', 
                'authors', 
                'title', 
                'url', 
                'journal', 
                'year', 
                'volume', 
                'issue', 
                'pages'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for publication in Publication.objects.all():
                writer.writerow({
                    'name': publication.name,
                    'publication_number': publication.publication_number,
                    'authors': publication.authors,
                    'title': publication.title,
                    'url': publication.url,
                    'journal': publication.journal,
                    'year': publication.year,
                    'volume': publication.volume,
                    'issue': publication.issue,
                    'pages': publication.pages,
                })

        self.stdout.write(self.style.SUCCESS(f'Successfully exported publications to {filename}'))
