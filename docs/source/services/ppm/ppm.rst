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

      Questionnaire file: ``PPM/Forms/Patient_Data/P10000/10000_2022-09-07-06-46-12.json``

      Metadata file: ``PPM/Forms/Metadata//P10000/10000_2022-09-07-06-46-12.json``


Important files
~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   important_files


APIs
~~~~

Upload patient API
+++++++++++++++++

:kbd:`POST /api/v1/ppm/upload_ppm_patient_to_s3`

   Upload the patient's questionnaire and metadata json files to S3 bucket.

   **Parameters**:

   :patients_data_ppm: json (required), A json object of the patient's questionnaire.

   :patients_metadata_ppm: json (required), A json object containing details about filling out the questionnaire.

   **Responses**:

   :statuscode 200: file uploaded successfully.
   :statuscode 500: The function get some error.
   :statuscode 404: There's an error in the input parameters.

   **Example request**:

   .. sourcecode:: python

      import requests
      import json
      from datetime import datetime
      URL = 'https://<NETWORK>/api/v1/ppm/upload_ppm_patient_to_s3'
      data = json.load(open('body.json', 'rb'))
      response = requests.post(
            URL,
            json=data
      )
      print(response.json())

   The content of ``body.json`` is like:

   .. sourcecode:: json

      {
         patient_json = {'2_Or_More_Chest_Cardiac_Ct_By_The_Age_Of_23': 1, 'Address': {'address': 'אבו סריחאן (שבט), אבו סריחאן (שבט)', 'city_id': 935}, 'At_Risk_Of_Contracting_Hiv': 0, 'Atherosclerosis_At_Young_Age_Relatives': 1, 'Average_Alcohol_Consumption': '3 glasses or more of alcoholic beverage per day', 'Blood_Transfusion_Before_1992': 0, 'Breast_Ovarian_Fallopian_Tube_Cancer_Now_Or_Past': 1, 'Cervical_Cancer_Now_Or_Past': 0, 'Colon_Cancer_Now_Or_Past': 1, 'Country_Of_Birth': 'Albania', 'Date_Of_Birth': '04.08.1989', 'Diagnosed_With_Osteoporosis': 0, 'Education': 'high school', 'F': 1, 'Felt_Depressed_Or_Despaired_Or_Hopeless_In_Past_Month': 0, 'Felt_Lake_Of_Interest_Or_Lack_Of_Pleasure_In_Past_Month': 1, 'Has_Diabetes': 0, 'Has_Hypertension': 1, 'Heart_Disease_At_Young_Age_Relatives': 0, 'Height': 163, 'Hmo': 'meuchedet', 'Hyperlipidemia_Relatives': 1, 'Is_Smoker': 0, 'Is_Smoking_Other_Stuff': 1, 'Know_Disease_That_Increases_Chance_Of_Osteoporotic_Fracture': 1, 'Lung_Cancer_Now_Or_Past': 1, 'M': 0, 'Main_Address_Last_5_Years': {'address': 'אבו סריחאן (שבט)', 'city_id': 935}, 'Marital_Status': 'married', 'Melanoma_Cancer_Now_Or_Past': 1, 'Number_Of_Children': 7, 'Origin': ['Christian Arab'], 'Past_Smoker': 0, 'Patient_Id': 123, 'Pregnant': 0, 'Steroid_Treatement_For_3_Month_Or_More': 0, 'Used_Drugs_By_Injection': 1, 'Weight': 51, 'Patient_Odm_Id': 140, 'Patient_Age': 33, 'Bmi': 19, 'Bmi_Above_30': 0, 'Bmi_Below_19': 1, 'Bmi_Above_25': 0, 'Bmi_Above_29': 0, 'Born_In_Ussr': 0, 'Did_Not_Receive_Complete_Israeli_Immunization': 0, 'Unvaccinated_For_Seasonal_Flu_This_Year': 0, 'Not_Received_Booster_For_Tetanus_In_Last_10_Years': 0, 'Not_Immune_To_Hepatitis_B': 0, 'More_Than_5_Years_Since_Last_Vaccine': 0, 'More_Than_Zero_Alcoholic_Drinks_Per_Day': 1, 'One_Or_More_Alcoholic_Drinks_Per_Day': 1, 'Two_Or_More_Alcoholic_Drinks_Per_Day': 1, 'Three_Or_More_Alcoholic_Drinks_Per_Day': 1, 'Born_Before_1992': 1, 'Blood_Pressure_Not_Measured_In_The_Last_Year': 1, 'Not_Done_A_Lipid_Profile_Test_In_The_Last_5_Years': 1, 'Yemeni_Or_Ethiopian_Ethnic_Background': 0, 'Ashkenazi_Or_Partial_Ashkenazi_Descent': 0, 'Not_Do_Sport': 1, 'Male_Aged_55_To_69': 0, 'Male_Aged_70+': 0, 'Aged_50+': 0, 'Not_Pregnant': 1, 'Late_Menopause': 0, 'Gave_Birth_After_35_Years_Old': 0, 'Not_Done_A_Pap_Test_In_The_Last_3_Years': 1, 'Not_Done_A_Hpv_Test_In_The_Last_3_Years': 0, 'Female_Aged_40_To_49': 0, '_key': '10000', 'Arango_DB_Indexing_Date': '2022-08-09-17-01-18', 'Got_Recommendations': 0},
         patient_metadata = {"patient_id": 123, "client": 'ayalon', "fill_date": datetime.now().strftime("%d-%m-%y-%H-%M-%S")}
      }

   Check out the :ref:`ppm-microservice` section for further information about the API implementation.

.. note::

   The following APIs are automatically executed following the upload_ppm_patient_to_s3 API.

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



Test profiles
~~~~~~~~~~~~~

1. Fill the profile's properties in the columns answers_2, answers_3.... in the format of answers_1

   `test profiles <https://drive.google.com/drive/folders/1qrHG9whHDsGynPJi1xeYroUQz4E1HPPz?usp=sharing>`_

2. Download the file as csv with the name : ``ppm_patients_test_cases.csv``

3. Upload the file to the S3 in the next path: ``s3://dev-machine-db/ppm/``

4. Run the 'run_test_profiles' API using the `swagger <http://dev-eu-central-1-ppm.dev.internal.od-machine.com/apidocs/#/>`_ 