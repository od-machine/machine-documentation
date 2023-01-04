update recommendations API
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