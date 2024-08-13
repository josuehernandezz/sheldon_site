from .models import Publication
from  .pub_data import publications_data

# Create Publication instances
publications_instances = [
    Publication(
        name=data['name'],
        publication_number=data['publication_number'],
        authors=data['authors'],
        title=data['title'],
        journal=data['journal'],
        year=data['year'],
        volume=data['volume'],
        pages=data['pages'],
        url=data['url']
    )
    for data in publications_data
]

# Bulk create the instances
Publication.objects.bulk_create(publications_instances)

# Output success message
print("Publications added successfully.")
