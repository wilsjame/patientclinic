import os
import dotenv
import geopy

dotenv.load_dotenv()
g = geopy.geocoders.GoogleV3(api_key=os.environ['GOOGLE_KEY'])

f = open('./data/patients.csv', 'r')
patient_data = list((f.read().split('\n')))
patient = {}

for line in patient_data:
    a = list(line.split(','))
    if a[0] == 'ID' or a[0] == '':
        continue

    assert(len(a) == 6), 'patient address details'
    # ex) 420,5811 BOUL TASCHEREAU BUREAU 100,J4Z 1A5,J4Z,BROSSARD,QC
    ID, address, postal_code, FSA, city, province = map(str, a)
    z = ' '.join([address, postal_code, FSA, city, province])
    location = g.geocode(z)
    geocode = {location.latitude, location.longitude}
    patient[ID] = geocode
