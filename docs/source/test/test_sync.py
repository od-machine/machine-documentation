def get_winter_patients_from_arango(client):
    '''
    get from arangoDB patients that haven't received recommendations
    :return patients - list of dicts with patients attributes
    '''
    pass

def get_patient_recommendations_edges(patient_id, edge_collection, arangoDB):
    '''
    get all patient's edges from arangoDB. if does not exist - return an empty list.
    :patient_id - string of the patient_id
    :edge_collection - name of the edge collection in arangoDB
    :return - edges list or [] if there is no edges
    '''
    pass

def summary_translate(patients):
    '''
    Function that receives a list of patients and creates from it a summary of the patient's health condition according to the patient's gender
    :patients - list of dicts with patients attributes
    :return summary_dict - dictionary with the patient's summary as string and the patient's gender
    '''
    pass

def create_recs_dict_to_letters(recommendations_data):
    '''
    The function removes attributes that are not relevant to the letters and returns them as JSON and drops duplicates from level 1 recommendations.
    :recommendations_data - {Patient_id1:[{key-value pairs with recommendation1 data},{key-value pairs with recommendation2 data}]},{Patient_id2:[{...}]} 
    :return recommendations_dict - recommendations_data after adjustments to the letters
    '''
    pass

def create_and_merge_edges(patient_id, recs_list, edges_date, edge_collection, existing_edges):
    '''
    create edges list according to the recs_list.
    create single edge for each recommendation id with date and causes (conditions and cities). 
    if there is a single recommendation and different conditions/cities list/origins list - apend the lists to the 'causes' property
    :patient_id - string of the patient_id
    :recs_list - list of dictionaries with recommendations details of single patient
    :edges_date - the date to write on the edges
    :edge_collection - name of the edge collection in arangoDB
    :return - edges_list - list of edges dictionaries, with merged recommendations in case of duplicate recommendations. 
    '''
    pass

def create_edges_list_to_arango(recommendations_data, arangoDB):
    '''
    create a list of edges that need to be created in the collection that maps recommendations to patients.
    :recommendations_data - {Patient_id1:[{key-value pairs with recommendation1 data},{key-value pairs with recommendation2 data}]},{Patient_id2:[{...}]} 
    :return edges_list_to_arango - list of edges to create / update in arangoDB
    :return edge_collection - the collection name (str) of the edges.
    '''
    pass



def create_recs_list_to_arango(recommendations_data):
    '''
    Function that receives a dictionary of patient_ids as keys and a list of dictionaries of recommendations as values.
    It create one list of the recommendations dictionaries with the relevant attributes.
    :recommendations_data - {Patient_id1:[{key-value pairs with recommendation1 data},{key-value pairs with recommendation2 data}]},{Patient_id2:[{...}]} 
    :return recommendations - list of dictionaries with recommendations attributes
    '''
    pass



def match_patients_conditions(general_conditions, age_conditions, patients):
    '''
    get conditions and patients data and match them
    :general_conditions - list of patient's general conditions ids
    :age_conditions - list of patient's age conditions ids
    :patients - list of patients details
    :return patients_conditions_cities_dict - dictionary of Patient_ids with their conditions_id and cities_id
    example of return -> {Patient_id1:{'cond_list':[cond_id1, cond_id2], 'cities_list':[city_id1, city_id2]}, Patient_id2:{'cond_list': ...}}
    '''
    pass



def get_recommendations_from_neo4j(conditions_list, cities_list, origins_list, graphDB):
    '''
    get from neo4j single patient recommendations details according to his conditions and cities.
    :conditions_list - patient's conditions ids list.
    :cities_list - patient's cities ids list.
    :return data - list of dictionaries, contains the patient recommendations details.
    '''
    pass



def parse_recommendations(patient_id, recommendations_data):
    '''
    parse single patient's recommendations to be flatten dictionary and give numbers for the references
    :patient_id - the current patient id
    :recommendations_data - list of dictionaries with recommendations details
    :return recommendations_data - the recommendations after flatting
    '''
    pass



def get_patients_recommendations_data(patient_conditions_and_cities, graphDB):
    '''
    create dictionary of patients recommendations.
    :patient_conditions_and_cities - dictionary of the patients, their conditions ids list and their cities ids list.
    :return patients_recommendations_data - dictionary of the patients and their recommendations details,
    the form of the retured dictionary is {patient_id1: [{}], patient_id2: [{}]}. 
    each inner list contains key&value of:
    risk_group_id, recommendation properties, reference properties, conditions_list, cities_list.
    '''
    pass



def get_patients_conditions_cities(patients, graphDB):
    """
    Function that creates dictionary of the patients and their conditions and cities.
    :patients - list of dicts with patients attributes 
    :return patients_conditions_cities_dict - dictionary of Patient_ids with their conditions_id and cities_id
    example of return -> {Patient_id1:{'cond_list':[cond_id1, cond_id2], 'cities_list':[city_id1, city_id2]}, Patient_id2:{'cond_list': ...}}
    """
    pass



def get_conditions_from_neo4j(graphDB):
    '''
    get from neo4j general and age conditions
    :return general_conditions - list of patient's general conditions ids
    :return age_conditions - list of patient's age conditions ids
    '''
    pass



def get_patients_from_arango(arangoDB):
    '''
    get from arangoDB patients that haven't received recommendations
    :return patients - list of dicts with patients attributes
    '''
    pass



def update_arango(recommendations_to_arango, edges_to_arango, arangoDB):
    '''
    Function that updates the arangoDB 'Recommendations' and edges collections
    :recommendations_to_arango - list of recs dictionaries to add Recommendations collection
    :edges_to_arango - list of edges dictionaries to add to the edges collection
    '''
    pass
