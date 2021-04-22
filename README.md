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

# analysis (nearest neighbor)
_P_ number of patients and _C_ number of clinics

startup, update: _O(1+2)_

- (1) **O((_P_ + _C_)(geocode query))**
- (2) **O(match nearest clinic for each patient)**
  - brute force: **O(_PC_)**
  - k-d tree: **O(_PlogC_)**
