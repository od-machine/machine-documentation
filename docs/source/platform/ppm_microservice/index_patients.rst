Index_Patients
==============

.. function:: read_json_file_from_s3(path_in_s3: str, bucketS3: object) -> dict

    Reads a JSON file from a specified path in an S3 bucket and returns the JSON object.

    :param path_in_s3: The file path to the JSON file in the S3 bucket.
    :type path_in_s3: str
    :param bucketS3: The S3 bucket object.
    :type bucketS3: object
    :return: The JSON object.
    :rtype: dict


.. function:: preprocess_patient(patient_json: dict, is_female_patient: int) -> dict

    Gets a patient's JSON, handles empty and "don't know" values, then creates all the complex conditions and adds some metadata.

    :param patient_json: The JSON patient object.
    :type patient_json: dict
    :param is_female_patient: Binary integer representing the patient's gender. 1 for female, 0 for male.
    :type is_female_patient: int
    :return: JSON with the preprocessed patient's data after all the complex conditions have been created.
    :rtype: dict


.. function:: index_patient_to_arangoDB(preprocessed_patient: dict, arangoDB: object) -> dict

    Receives a patient JSON and indexes it inside the 'Patient' collection in an ArangoDB instance.

    :param preprocessed_patient: JSON that holds all the patient's data after preprocessing.
    :type preprocessed_patient: dict
    :param arangoDB: ArangoDB object that holds the connection to the DB.
    :type arangoDB: object
    :return: JSON that holds all the patient's data after preprocessing, including indexing metadata.
    :rtype: dict


.. function:: sort_files_by_date(files_list: list, date_format: str) -> list

    Sorts a list of file paths by their date in ascending order.

    :param files_list: List of file paths.
    :type files_list: list
    :param date_format: The format of how the date is saved in the file path.
    :type date_format: str
    :return: List of file paths sorted by date in ascending order.
    :rtype: list


.. function:: move_files_to_archive(patient_id: int, patient_path: str, metadata_path: str, patient_file_name: str, patient_json_metadata: dict, bucketS3: object)

    Moves a patient's JSON file from the 'Forms' directory to the 'Archived_Forms' directory and moves the patient's metadata JSON file from the 'Forms' directory to the 'Recommendations' directory.

    :param patient_id: The patient's ID.
    :type patient_id: int
    :param patient_path: The file path of the patient's JSON file.
    :type patient_path: str
    :param metadata_path: The file path of the patient's metadata JSON file.
    :type metadata_path: str
    :param patient_file_name: The file name of the patient's JSON file, without the full path or extension.
    :type patient_file_name: str
    :param patient_json_metadata: The patient's metadata JSON object.
    :type patient_json_metadata: dict
    :param bucketS3: The S3 bucket object.
    :type bucketS3: object


.. function:: validations(indexed_patient_id: int, patient_id_from_file_name: str, patient_json_metadata: dict, patient_path: str, arangoDB: object)

    Validates the patient ID, verifies that the patient's JSON has been correctly uploaded to the 'Patients' collection, and validates that the patient's metadata JSON has been correctly uploaded to the 'Recommendations' collection.

    :param indexed_patient_id: The patient ID that was uploaded to ArangoDB.
    :type indexed_patient_id: int
    :param patient_id_from_file_name: The patient ID from the patient file name.
    :type patient_id_from_file_name: str
    :param patient_json_metadata: The patient's metadata JSON object.
    :type patient_json_metadata: dict
    :param patient_path: The file path of the patient's JSON file.
    :type patient_path: str
    :param arangoDB: The ArangoDB object holding the connection to the DB.
    :type arangoDB: object


.. function:: scan_new_patients(client: object)

    Wrapper function that indexes multiple patients to an ArangoDB instance.

    :param client: The AWS client object.
    :type client: object


.. function:: create_odm_id(patient_json: dict, postgreSQL_db_hendler: object) -> dict

    Gets a patient's JSON, adds it to a PostgreSQL database to get an ODM ID, then adds the ODM ID to the patient JSON.

    :param patient_json: JSON of the patient's answers (preprocessed).
    :type patient_json: dict
    :param postgreSQL_db_hendler: Object that handles interactions with the PostgreSQL database.
    :type postgreSQL_db_hendler: object
    :return: JSON of the patient's answers with the new ODM ID.
    :rtype: dict


.. function:: index_single_patient(patient_path: str, host_client: object, client: object, failed_patient: bool = False)

    Gets a single patient file key in an S3 bucket, reads the answers file and the metadata file, and indexes the patient to an ArangoDB instance.

    :param patient_path: S3 path of the patient's answers file.
    :type patient_path: str
    :param host_client: The AWS EC2 host client object.
    :type host_client: object
    :param client: The AWS client object.
    :type client: object
    :param failed_patient: Boolean indicating whether the patient was a previously failed patient. Default is False.
    :type failed_patient: bool, optional