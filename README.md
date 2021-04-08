# Match a patient to their nearest clinic.

# Input
- Pair of csv files: patients.csv and clinics.csv
- Containing address details of each patient and clinic respectively

# Output 
- A csv file with number of rows equal to number of patients
- Each row indicates the nearest clinic to the corresponding patient

# what it does
- find geocode of each address 
- latitude and longitude of each address

- use geocodes to find clinic nearest to each individual patient
- based off travel/commute distance (and not the straight line distance)

# analysis 
startup, update: *O(1+2+3)*

- (1) **O((2 * rows)(geocode query + update))**
- (2) **O((2 * rows)(travel commute distance compute + update))**
- (3) **O(match nearest clinic for each patient)**
 - brute force: **O(rows <sup>2</sup> * distance query)**

query: *O(const)*

