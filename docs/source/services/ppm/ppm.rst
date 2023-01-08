PPM
===
A product to provide health insurance policy holders with individualized recommendations for diagnostic testing, promoting preventive and personalized health.

.. image:: ppm_flow.png


Architecture
~~~~~~~~~~~~

.. image:: ppm_architecture.png


Prerequisites
~~~~~~~~~~~~~

1. Medical recommendations data should be indexed onto the neo4j graph.

   .. image:: ppm_graph.png

   * Data for the recommendations was taken from several sources, the majority came from the MOH 2022 recommendation document.

   * In addition to the recommendations, there are links to articles and links that provide further information.

   * Every recommendation is tailored to specific groups of the population based on a number of factors, such as their age (minimum/maximum), gender, biochemical variables, and other factors.

2. Both the questionnaire file and the metadata file should be in the correct place in S3.

   For example for patient number 10000 that uploaded to S3 in 9/7/22 6:46:12 the S3 hierarchy is:

      Questionnaire file: ``PPM/Forms/Patient_Data/P10000/10000_2022-09-07-06-46-12.json``ß

      Metadata file: ``PPM/Forms/Metadata//P10000/10000_2022-09-07-06-46-12.json``

APIs
~~~~

Index patient API
+++++++++++++++++

:kbd:`POST /api/v1/ppm/index_ppm_patient`

   Index the patient's questionnaire details from S3 bucket to the ArangoDB.

   **Parameters**:

   :path_patient_details: string (required), Path to the patient details in S3 bucket.

   :client: string (required), The client name.

   :host_client: string (required), The host client name.

   **Responses**:

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

   The content of ``body.json`` is like:

   .. sourcecode:: json

      {
         "path_patient_details": "PPM/Forms/Patient_Data/P10000/10000_2022-09-07-06-46-12.json",
         "host_client": "host_client_name", 
         "client": "client_name"
      }

   Check out the :ref:`ppm-microservice` section for further information about the API implementation.


Update recommendations API
++++++++++++++++++++++++++

:kbd:`POST /api/v1/ppm/update_patients_conditions_and_recommendations`

   Creates recommendations files and uploads them to the S3 bucket.

   **Parameters**:

   :path_patient_details: string (required), Path to the patient details in S3 bucket.

   :client: string (required), The client name.

   :host_client: string (required), The host client name.

   **Example response**:

   :statuscode 200: Successfully updated the patients.
   :statuscode 500: The function get error.
   :statuscode 404: There's an error in the input parameters.

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

   The content of ``body.json`` is like:

   .. sourcecode:: json

      {
         "host_client": "host_client_name", 
         "client": "client_name"
      }

   Check out the :ref:`sync-microservice` section for further information about the API implementation.
