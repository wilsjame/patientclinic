import os
import dotenv
import geopy

dotenv.load_dotenv()
g = geopy.geocoders.GoogleV3(api_key=os.environ['GOOGLE_KEY'])

with open('./data/patients.csv', 'r') as f:
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

with open('./data/clinics.csv', 'r') as f:
    clinic_data = list(f.read().split('\n'))
clinic = {}
for line in clinic_data:
    a = list(line.split(','))
    if a[0] == 'Clinic ID' or a[0] == '':
        continue
    assert(len(a) == 7), 'clinic address details'
    # ex) 69,Clinic 69,34 Cedar Pointe Dr Unit 505,L4N 5R7,L4N,Barrie,ON
    ID, clinic_name, address, postal_code, FSA, city, province = map(str, a)
    z = ' '.join([address, postal_code, FSA, city, province])
    location = g.geocode(z)
    geocode = {location.latitude, location.longitude}
    clinic[ID] = geocode

