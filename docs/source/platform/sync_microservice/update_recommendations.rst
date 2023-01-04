Update_Recommendation functions
===============================

.. function:: get_winter_patients_from_arango(client: Type[ArangoClient]) -> List[Dict[str, Any]]

    Get from arangoDB patients that haven't received recommendations.

    :param client: ArangoClient object for connecting to the database.
    :type client: Type[ArangoClient]
    :return: list of dictionaries with patients attributes.
    :rtype: List[Dict[str, Any]]


.. function:: get_patient_recommendations_edges(patient_id: str, edge_collection: str, arangoDB: ArangoDB) -> List[Dict[str, Any]]

    Get all patient's edges from arangoDB. If does not exist, return an empty list.

    :param patient_id: string of the patient's id.
    :type patient_id: str
    :param edge_collection: name of the edge collection in arangoDB.
    :type edge_collection: str
    :param arangoDB: ArangoDB object for executing AQL queries and accessing the graph.
    :type arangoDB: ArangoDB
    :return: edges list or [] if there is no edges.
    :rtype: List[Dict[str, Any]]


.. function:: summary_translate(patients: List[Dict[str, Any]]) -> Dict[str, Union[str, List[str]]]

    Function that receives a list of patients and creates from it a summary of the patient's health condition according to the patient's gender.

    :param patients: list of dictionaries with patients attributes.
    :type patients: List[Dict[str, Any]]
    :return: dictionary with the patient's summary as string and the patient's gender.
    :rtype: Dict[str, Union[str, List[str]]]


.. function:: create_recs_dict_to_letters(recommendations_data)

    This function takes in a dictionary of recommendations data, with the format {Patient_id1:[{key-value pairs with recommendation1 data},{key-value pairs with recommendation2 data}]},{Patient_id2:[{...}]}, and processes it to be used in letters. It removes unnecessary attributes and drops duplicates from level 1 recommendations.

    :type recommendations_data: dict
    :param recommendations_data: The dictionary of recommendations data for each patient.

    :return: The processed recommendations data, in the same format as the input.


.. function:: create_and_merge_edges(patient_id, recs_list, edges_date, edge_collection, existing_edges)

    This function creates a list of edges, connecting a patient to their recommendations, according to the provided recommendations data. It also merges recommendations with the same id and different causes (conditions and cities).

    :type patient_id: str
    :param patient_id: The id of the patient the edges will be connecting to.

    :type recs_list: list
    :param recs_list: A list of dictionaries with recommendations data for a single patient.

    :type edges_date: str
    :param edges_date: The date to write on the edges.

    :type edge_collection: str
    :param edge_collection: The name of the edge collection in the arangoDB database.

    :type existing_edges: list
    :param existing_edges: A list of existing edges for the patient, or an empty list if there are no existing edges.

    :return: A list of dictionaries representing the edges, with merged recommendations in case of duplicate recommendations.


.. function:: create_edges_list_to_arango(recommendations_data:dict, arangoDB:object) -> Tuple[List[Dict[str,Union[str,int]]], str]

    This function creates a list of edges that need to be created in the collection that maps recommendations to patients in arangoDB.

    :param recommendations_data: a dictionary with patient ids as keys and a list of dictionaries of recommendations as values.
    :type recommendations_data: dict
    :param arangoDB: an object of the arangoDB connection
    :type arangoDB: object
    :return: a tuple containing a list of edges to create/update in arangoDB and the collection name (str) of the edges.
    :rtype: Tuple[List[Dict[str,Union[str,int]]], str]


.. function:: create_recs_list_to_arango(recommendations_data:dict) -> List[Dict[str,Union[str,int]]]

    This function receives a dictionary of patient_ids as keys and a list of dictionaries of recommendations as values. It creates one list of the recommendations dictionaries with the relevant attributes.

    :param recommendations_data: a dictionary with patient ids as keys and a list of dictionaries of recommendations as values.
    :type recommendations_data: dict
    :return: a list of dictionaries with recommendations attributes.
    :rtype: List[Dict[str,Union[str,int]]]

.. function:: match_patients_conditions(general_conditions:List[Dict[str,Union[str,int]]], age_conditions:List[Dict[str,Union[str,int]]], patients:List[Dict[str,Union[str,int]]]) -> Dict[str,Dict[str,List[Union[str,int]]]]

    This function receives conditions and patients data and matches them. It returns a dictionary with patient ids as keys and a dictionary containing the patient's conditions_id and cities_id as values.

    :param general_conditions: a list of patient's general conditions ids.
    :type general_conditions: List[Dict[str,Union[str,int]]]
    :param age_conditions: a list of patient's age conditions ids.
    :type age_conditions: List[Dict[str,Union[str,int]]]
    :param patients: a list of patients details.
    :type patients: List[Dict[str,Union[str,int]]]
    :return: a dictionary of patient_ids with their conditions_id and cities_id.
    :rtype: Dict[str,Dict[str,List[Union[str,int]]]]


.. function:: get_recommendations_from_neo4j(conditions_list, cities_list, origins_list, graphDB)
    
    This function retrieves single patient recommendations details from neo4j according to the patient's conditions and cities.
    
    :param conditions_list: A list of patient's conditions IDs.
    :type conditions_list: List[str]
    :param cities_list: A list of patient's cities IDs.
    :type cities_list: List[str]
    :param origins_list: A list of patient's origins names.
    :type origins_list: List[str]
    :param graphDB: A Graph object representing the neo4j database.
    :type graphDB: Graph
    :return: A list of dictionaries, each containing the patient recommendations details.
    :rtype: List[Dict]

.. function:: parse_recommendations(patient_id, recommendations_data)
    
    This function takes a patient ID and a list of dictionaries of recommendations details, and flattens the recommendations data and gives numbers for the references.
    
    :param patient_id: A string of the patient ID.
    :type patient_id: str
    :param recommendations_data: A list of dictionaries with recommendations details.
    :type recommendations_data: List[Dict]
    :return: The recommendations data after flattening.
    :rtype: List[Dict]


.. function:: get_patients_recommendations_data(patient_conditions_and_cities, graphDB)
    
    This function creates a dictionary of patients recommendations.
    
    :param patient_conditions_and_cities: A dictionary of the patients, their conditions IDs list, and their cities IDs list.
    :type patient_conditions_and_cities: Dict[str, Dict[str, Union[str, List[str]]]]
    :param graphDB: A Graph object representing the neo4j database.
    :type graphDB: Graph
    :return: A dictionary of the patients and their recommendations details. The form of the returned dictionary is {patient_id1: [{}], patient_id2: [{}]}, where each inner list contains key-value pairs for the following: risk_group_id, recommendation properties, reference properties, conditions_list, cities_list.
    :rtype: Dict[str, List[Dict[str, Union[str, List[str]]]]]


.. function:: get_patients_conditions_cities(patients: List[Dict], graphDB: Graph) -> Dict[str, Dict[str, Union[List[str], List[int]]]]:

    This function creates a dictionary of patients and their conditions and cities.

    :param patients: A list of dictionaries with patients attributes.
    :type patients: List[Dict]
    :param graphDB: A Graph object representing the neo4j database.
    :type graphDB: Graph
    :return: A dictionary of patient IDs with their conditions IDs and cities IDs.
    :rtype: Dict[str, Dict[str, Union[List[str], List[int]]]]

.. function:: get_conditions_from_neo4j(graphDB: Graph) -> Tuple[List[Dict], List[Dict]]:

    This function retrieves general and age conditions from neo4j.

    :param graphDB: A Graph object representing the neo4j database.
    :type graphDB: Graph
    :return: A tuple containing a list of patient's general conditions IDs and a list of patient's age conditions IDs.
    :rtype: Tuple[List[Dict], List[Dict]]


.. function:: get_patients_from_arango(arangoDB: Client) -> List[Dict]:
    
    This function retrieves patients that haven't received recommendations from arangoDB.
    
    :param arangoDB: An instance of the arangoDB client.
    :type arangoDB: Client
    :return: A list of dictionaries with patients attributes.
    :rtype: List[Dict]


.. function:: update_arango(recommendations_to_arango: List[Dict], edges_to_arango: List[Dict], arangoDB: Client)
    
    This function updates the arangoDB 'Recommendations' and edges collections.
    
    :param recommendations_to_arango: A list of recommendations dictionaries to add to the Recommendations collection.
    :type recommendations_to_arango: List[Dict]
    :param edges_to_arango: A list of edges dictionaries to add to the edges collection.
    :type edges_to_arango: List[Dict]
    :param arangoDB: An instance of the arangoDB client.
    :type arangoDB: Client


.. function:: update_recommendations_proccess(host_client, client)
    
    This function updates the recommendations for patients in arangoDB and creates a list of recommendations dictionaries for the pdf.
    
    :param host_client: The host client for connecting to arangoDB.
    :type host_client: str
    :param client: The client for connecting to arangoDB.
    :type client: ArangoClient
    :return: A dictionary of recommendations data for the pdf, with the format {Patient_id1:[{key-value pairs with recommendation1 data},{key-value pairs with recommendation2 data}]},{Patient_id2:[{...}]}.
    :rtype: Dict[str, List[Dict]]
