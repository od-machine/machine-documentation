index patient API
+++++++++++++++++

:kbd:`POST /api/v1/ppm/index_ppm_patient`

   Index the patient's questionaire details from S3 bucket to the ArangoDB.

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