PPM
===
A product to provide health insurance policyholders with individualized recommendations for diagnostic testing, promoting preventive and personalized health.

.. image:: ppm_flow.png


Prerequisites
~~~~~~~~~~~~~

Medical recommendations data should be indexed onto the neo4j graph.

.. image:: ppm_graph.png

Data for the recommendations was taken from several sources, but the majority came from the MOH 2022 recommendation document, along with references and links to the reference articles for further information.

Every recommendation is tailored to specific groups of the population based on a number of factors, such as their age (minimum/maximum), gender, biochemical variables, and other factors.



APIs
~~~~

index patient API
+++++++++++++++++

:kbd:`POST /api/v1/ppm/index_ppm_patient`

   Index the patient's questionaire details from S3 bucket to the ArangoDB.

   Check out the :doc:`PPM-Microservice <docs/source/platform/ppm_microservice/ppm_microservice.rst>` section for further information about the API implementation.

   **Parameters**:

      - path_patient_details: string (required)
      Description: Path to the patient details in S3 bucket.

      - client: string (required)
      Description: The client name

      - host_client: string (required)
      Description: The host client name


   **Response**:

   :statuscode 200: The patient index's has been successful.
   
   :statuscode 500: The function get some error.

   :statuscode 404: There's an error in the input parameters.


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
