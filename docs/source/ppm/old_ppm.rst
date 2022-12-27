PPM
===
A product to provide health insurance policyholders with individualized recommendations for diagnostic testing, promoting preventive and personalized health.

.. image:: ppm_flow.png


.. contents:: PPM's repositories
   :local:
   :backlinks: none
   :depth: 3


Machine-DB
~~~~~~~~~~

Index of the medical recommendations for the graph.

1. The recommendations are taken from multiple sources, the largest data was taken from the MOH recommendation document 

2. For each recommendation we also have a reference and link to the reference article that our recommendation is based on. 

3. Each recommendation is fit to specific groups in the population according to a lot of properties such as: age (min/max), gender,family history of illness, and other environmental variables, place of residence, odm_id etc.


.. image:: ppm_graph.png


PPM-Microservice
~~~~~~~~~~~~~~~~~

The purpose of this microservice is upload the patients data to ArangoDB.

index patient API
+++++++++++++++++

:kbd:`POST /api/v1/ppm/index_ppm_patient`

   Index the patient's questionaire details to the ArangoDB.

   **Example request**:

   .. sourcecode:: python

      import requests
      import json
      URL = 'https://<NETWORK>/api/v1/ppm/index_ppm_patient'
      data = json.load(open('body.json', 'rb'))
      response = requests.post(
            URL,
            json=data
      )
      print(response.json())

   The content of ``body.json`` is like,

   .. sourcecode:: json

      {
         "path_patient_details": "PPM/Forms/Patient_Data/P10000/10000_2022-09-07-06-46-12.json",
         "host_client": "femi", 
         "client": "ayalon"
      }

   **Example response**:

   :statuscode 200: The patient index's has been successful


Sync-Microservice
~~~~~~~~~~~~~~~~~

The purpose of this microservice is to match each patient with the recommendations intended for him, to upload recommendations to S3 and to create connections between the patients and their recommendations in ArangoDB.

update recommendations API
++++++++++++++++++++++++++

:kbd:`POST /api/v1/ppm/update_patients_conditions_and_recommendations`

   Index the patient's questionaire details to the ArangoDB.

   **Example request**:

   .. sourcecode:: python

      import requests
      import json
      URL = 'https://<NETWORK>/api/v1/ppm/update_patients_conditions_and_recommendations'
      data = json.load(open('body.json', 'rb'))
      response = requests.post(
            URL,
            json=data
      )
      print(response.json())

   The content of ``body.json`` is like,

   .. sourcecode:: json

      {
         "host_client": "femi", 
         "client": "ayalon"
      }

   **Example response**:

   :statuscode 200: Successfully updated the patients
