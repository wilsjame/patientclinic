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
_P_ number of patients and _C_ number of clinics

startup, update: _O(1+2+3)_ = _O((PC)<sup>2</sup>(P+C))_ = _O(P<sup>3</sup>C<sup>2</sup> + C<sup>3</sup>P<sup>2</sup>)_ = _O(P<sup>3</sup> + C<sup>3</sup>)_

- (1) **O((_P_ + _C_)(geocode query))**
- (2) **O((_PC_)(distance query))**
- (3) **O(match nearest clinic for each patient)**
  - brute force: **O(_PC_)(distance lookup)**

match lookup: _O(const)_
