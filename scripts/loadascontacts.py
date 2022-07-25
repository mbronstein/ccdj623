from contacts.models import AsContact
import csv
import os


def run():
    print('cwd=', os.getcwd())
    with open('testasc.csv') as file:
        reader = csv.reader('testasc.csv')
        next(reader)  # Advance past the header

        AsContact.objects.all().delete()

        for row in reader:
            print('row=', row)

            contact = AsContact(name=row[0],
                                address=row[1],
                                city=row[2],
                                state=row[3],
                                zip=row[4],
                                email=row[5],
                                phone=row[6],
                                )
            contact.save()
