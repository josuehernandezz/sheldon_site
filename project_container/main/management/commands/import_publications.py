import csv
from django.core.management.base import BaseCommand
from main.models import Publication

class Command(BaseCommand):
    help = 'Import publications from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            publications = []
            for row in reader:
                try:
                    publication = Publication(
                        name=row['name'],
                        publication_number=int(row['publication_number']) if row['publication_number'] else None,
                        authors=row['authors'],
                        title=row['title'],
                        url=row['url'],
                        journal=row['journal'],
                        year=int(row['year']) if row['year'] else None,
                        volume=int(row['volume']) if row['volume'] else None,
                        issue=int(row['issue']) if row['issue'] else None,
                        pages=row['pages']
                    )
                    publications.append(publication)
                except KeyError as e:
                    self.stderr.write(self.style.ERROR(f'Missing key: {str(e)} in row: {row}'))
                except ValueError as e:
                    self.stderr.write(self.style.ERROR(f'Invalid value for publication: {row}, error: {str(e)}'))

            # Bulk create Publication instances
            Publication.objects.bulk_create(publications)

        self.stdout.write(self.style.SUCCESS('Successfully imported publications'))
