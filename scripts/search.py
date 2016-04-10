import pandas as pd
import re
import geocoder

data = pd.read_csv('resources/Canadian Arctic Archipelago.csv')

def convert_dms(coord):
    match = re.search(r'(\d+)\D+(\d+)\D+([NSWE])', coord)
    if match:
        degree, minutes, direction = match.groups()
        degree, minutes = float(degree), float(minutes)
        dms = degree + minutes / 60.0

        if direction in ['N', 'E']:
            return dms
        elif direction in ['W', 'S']:
            return -1 * dms

print 'name,lat,lng,distance,lat-osm,lng-osm'
for index, row in data.iterrows():
    g = geocoder.osm(row['name'])
    distance = geocoder.distance(g.latlng, [row['lat'], row['lng']])
    print '{},{},{},{},{},{}'.format(
        row['name'],
        row['lat'],
        row['lng'],
        distance,
        g.lat,
        g.lng
    )
