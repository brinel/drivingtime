import googlemaps
import csv
from datetime import datetime
import os
apikey = os.environ['GAPI_KEY']

gmaps = googlemaps.Client(key=apikey)

with open('results.csv', 'w', newline='') as resultfile:
    with open('zipslatlong.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            zipcode = row[0]
            origin = row[1]
            destination = row[2]

            directions_result = gmaps.distance_matrix(origin, destination)

            csvwriter = csv.writer(resultfile, delimiter=',')
            csvwriter.writerow([zipcode, origin, destination, directions_result['rows'][0]['elements'][0]['duration']['value']])