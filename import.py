from app import app, db
from app.models import Location
import csv

def main():
    file_name = 'zips.csv'

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        total = sum([1 for row in reader])

        csvfile.seek(0)
        next(reader) # skip header

        count = 0
        for row in reader:
            location = Location(
                zipcode=row['Zipcode'], 
                city=row['City'], 
                state=row['State'], 
                latitude=float(row['Lat']),
                longitude=float(row['Long']),
                population=int(row['Population']))
            
            db.session.add(location)
            db.session.commit()

            # track progress
            count+=1
            print(f'{100*count/total:.2f} percent complete              ', end="\r")


if __name__ == '__main__':
    main()