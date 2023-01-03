* *index ppm patient* API

API to index the patient's questionaire details to the ArangoDB.


**run example**:

url: ``http://<NETWORK>:<PORT>/api/v1/ppm/index_ppm_patient``

data= ``{'path_patient_details': 'PPM/Forms/Patient_Data/P111/111_2022-09-07-06-46-12.json'}``


**actions**:

1. Gets from the request the patient's JSON path in S3.

2. Indexes the patient to ArangoDB

3. Calls SQS function to run the next API