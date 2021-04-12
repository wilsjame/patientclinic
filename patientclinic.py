import os
import time
import dotenv
import geopy

dotenv.load_dotenv()
g = geopy.geocoders.GoogleV3(api_key=os.environ['GOOGLE_KEY'])

# patient geocode data
with open('./data/patients.csv', 'r') as f:
    patient_data = list((f.read().split('\n')))

patient = {}
q_cnt = 0
for line in patient_data:
    a = list(line.split(','))
    if a[0] == 'ID' or a[0] == '':
        continue

    # ex) 420,5811 BOUL TASCHEREAU BUREAU 100,J4Z 1A5,J4Z,BROSSARD,QC
    assert(len(a) == 6), 'patient address details'
    ID, address, postal_code, FSA, city, province = map(str, a)

    # remove address elements to improve geocode result
    x = ['UNIT', 'ROOM', 'SUITE', 'FLOOR', 'BUREAU', 'PAVILION']
    for remove in x:
        address = address.split(remove)[0]
    z = ' '.join([address, postal_code, FSA, city, province])

    #TODO geocode fail, check return
    location = g.geocode(z)
    geocode = (location.latitude, location.longitude)
    patient[ID] = geocode
    # 50 QPS limit
    q_cnt += 1
    if q_cnt % 50 == 0:
        time.sleep(1)

with open('./patient_geocode') as f:
    f.write('PATIENT ID, LATITUDE LONGITUDE')
    for k in patient:
        f.write('{0}, {1} {2}'.format(k, patient[k][0], patient[k][1]))

# clinic geocode data
with open('./data/clinics.csv', 'r') as f:
    clinic_data = list(f.read().split('\n'))

clinic = {}
for line in clinic_data:
    a = list(line.split(','))
    if a[0] == 'Clinic ID' or a[0] == '':
        continue

    # ex) 69,Clinic 69,34 Cedar Pointe Dr Unit 505,L4N 5R7,L4N,Barrie,ON
    assert(len(a) == 7), 'clinic address details'
    ID, clinic_name, address, postal_code, FSA, city, province = map(str, a)

    # remove address elements to improve geocode results
    x = ['UNIT', 'ROOM', 'SUITE', 'FLOOR', 'BUREAU', 'PAVILION']
    for remove in x:
        address = address.split(remove)[0]
    z = ' '.join([address, postal_code, FSA, city, province])

    #TODO geocode fail, check return
    location = g.geocode(z)
    geocode = (location.latitude, location.longitude)
    clinic[ID] = geocode
    # 50 QPS limit
    q_cnt += 1
    if q_cnt % 50 == 0:
        time.sleep(1)

with open('./clinic_geocode') as f:
    f.write('CLINIC ID, LATITUDE LONGITUDE')
    for k in clinic:
        f.write('{0}, {1} {2}'.format(k, clinic[k][0], clinic[k][1]))
