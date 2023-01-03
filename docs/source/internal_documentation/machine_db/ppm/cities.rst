Cities
======

.. function:: remove_city_condition
---
    Remove conditions cities that created by conditions.py

    :return: None


.. function:: get_df_from_s3
---
    Read a CSV file from an S3 bucket and return a data frame containing its contents.

    :param path: path to csv file in s3
    :type path: str
    :return: data frame that readed from s3


.. function:: connect_cities_and_areas
---
    Create a list of dictionaries representing relationships between cities and areas.

    :param cities_and_areas_df: data frame with cities and area data
    :type cities_and_areas_df: pandas.DataFrame
    :return: list of dictionaries of the relations


.. function:: parse_index_stats_areas
---
    Create a list of dictionaries representing statistical areas.

    :param cities_and_areas_df: data frame with cities and area data
    :type cities_and_areas_df: pandas.DataFrame
    :return: list of dictionaries of the areas


.. function:: parse_index_cities
---
    Create a dictionary of dictionaries and a list of dictionaries representing cities and relationships between cities and their statistical areas.

    :param cities_and_areas_df: data frame with cities and area data
    :type cities_and_areas_df: pandas.DataFrame
    :return: dictionary of dictionaries of all cities and their details
    :return: list of dictionaries of the cities


.. function:: upload_geographic_data
---
    Upload all the cities, statistical areas and the relations to risk groups to the graph.

    :param cities_list: to create City nodes
    :type cities_list: list of dictionaries
    :param poll_cities_risk_group: to create relations to air pollution risk groups
    :type poll_cities_risk_group: list of dictionaries
    :param diseases_cities_and_risk_groups_list: to create relations to high risk to diseases risk groups
    :type diseases_cities_and_risk_groups_list: list of dictionaries
    :return: None
    :raises: Exception if an error occurs while accessing the graph database or logging


.. function:: load_diseases_df_from_s3
---
    Get the diseases data frame from s3, change columns names, and change city id column to number.

    :return: the data frame after the adjustments
    :raises: Exception if an error occurs while reading from the S3 bucket or logging


.. function:: load_cities_df_from_s3
---
    Load the cities data frames from s3 to dict and load the thresholds dict from s3.

    :return: dictionary of data farme, when the keys are years
    :return: thresholds dict (env val and target val for each pollutant)
    :raises: Exception if an error occurs while reading from the S3 bucket or parsing the thresholds file


.. function:: add_polluted_city_to_conditions
---
    Parse the polluted cities that higher than the environment value.

    :param cities_dict: dictionary of dictionaries - all cities and their details
    :type cities_dict: dict
    :param df: air pollution data per cities data frame
    :type df: pandas dataframe
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :type air_pollution_thresholds: dict
    :return: dictionary of all cities and their details - updated with polluted cities
    :raises: Exception if an error occurs while logging


.. function:: create_polluted_city_by_env_val
---
    Check for polluted city that higher than the environment value.

    :param cities_dict: dictionary of dictionaries - all cities and their details
    :type cities_dict: dict
    :param cities_df_dict: dictionary of data frame, when the keys are years
    :type cities_df_dict: dict
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :type air_pollution_thresholds: dict
    :return: dictionary of all cities and their details - updated with polluted cities
    :raises: Exception if an error occurs while logging


.. function:: create_stdv_for_pollutant
---
    Create standard deviation for each pollutant across all years.

    :param cities_df_dict: dictionary of data frame, when the keys are years
    :type cities_df_dict: dict
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :type air_pollution_thresholds: dict
    :return: dictionary of target value per pollutant after creating 2 units of standard deviation of all cities per all years
    :raises: Exception if an error occurs while logging


.. function:: pollutant_city_weighted_average
    Calculates the weighted average of an air pollution value per city.

    :param df: air pollution data after group by of specific city
    :param values: pollution value
    :param weights: the weights of creating weighted average
    :return: the weighted average
    :raises: Exception if an error occurs while logging


.. function:: create_df_weighted_average
    Creates a data frame of the weighted average of all cities in a single year.

    :param df: air pollution data per cities data frame
    :param target_stdv_pol_dict: dictionary of target value per pollutant after creating 2 units of standard deviation of all cities per all years
    :return: the weighted average
    :raises: Exception if an error occurs while logging


.. function:: cities_up_target_per_year
    Parses cities that have a higher target value in a specific year.

    :param target_stdv_pol_dict: dictionary of target value per pollutant after creating 2 units of standard deviation of all cities per all years
    :param weight_df: data frame of all cities after calculate their weighted average per pollutant
    :return: list of the cities that higher than target value in specific year
    :raises: Exception if an error occurs while logging


.. function:: cities_list_no_returns
    Returns a list of cities that have no returns in a specific year.

    :param cities: list of cities
    :param no_returns_df: data frame of cities that have no returns
    :return: list of the cities that have no returns in a specific year
    :raises: Exception if an error occurs while logging


.. function:: create_polluted_city_by_target_val(cities_dict, cities_df_dict, air_pollution_thresholds)

    Given a dictionary of all cities and their details, a dictionary of data frames where the keys are years, and a thresholds dictionary (environmental values and target values for each pollutant), this function parses the polluted cities that are 2 standard deviation units higher than the target value across all the years and at least 3 pollutants. It returns an updated dictionary of all cities and their details, as well as a set of the polluted cities.

    :param cities_dict: dictionary of dictionaries - all cities and their details
    :param cities_df_dict: dictionary of data frame, where the keys are years
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :return: cities_dict - dictionary of all cities and their details - updated with polluted cities
    :return: pol_cities - set of the polluted cities


.. function:: parse_relations_poll_cities_risk(pol_cities)

    Given a set of polluted cities, this function parses the relation between the risk group and polluted cities. It returns a list of dictionaries to create the relations.

    :param pol_cities: set of the polluted cities
    :return: risk_poll_relations - list of dictionaries to create the relations


.. function:: get_disease_city_dict(disease_df, disease_name)

    Given a data frame of all the diseases and a disease name, this function finds the cities with a high risk for the given disease. It returns a dictionary of the form {disease: [{'shem_yshuv': city_name1, 'yshuv': city_id1}]}.

    :param disease_df: data frame of all the diseases
    :param disease_name: the name of disease to find relevant cities
    :return: dictionary of the form {disease: [{'shem_yshuv': city_name1, 'yshuv': city_id1}]}


.. function:: update_diseases_in_cities_dict(cities_dict, city_diseases_dict)

    Update the given cities_dict with diseases that are at high risk in the city.

    :param cities_dict: A dictionary of dictionaries, representing all cities and their details.
    :param city_diseases_dict: A dictionary of the diseases and cities with high risk to the disease.
    :return: The updated cities_dict with the diseases added to it.


.. function:: add_diseases_to_cities(cities_dict, disease_df)

    Read the disease_df and add the diseases as properties to cities with high risk to the diseases.

    :param cities_dict: A dictionary of dictionaries, representing all cities and their details.
    :return: The updated cities_dict with the diseases added to it, and a dictionary of the form {disease: [{'shem_yshuv': city_name1, 'yshuv': city_id1}]}.


.. function:: parse_relations_diseases_cities_risk(diseases_cities_dict)

    Parse the relation between risk group and cities with high risk to diseases.

    :param cities_with_diseases_dict: A dictionary of the form {disease: [{'shem_yshuv': city_name1, 'yshuv': city_id1}]}.
    :return: A list to create the relationships.


.. function:: index_cities_and_areas()

    Index the cities, statistical areas and relations to the graph.

    This function will do the following:

    * Remove city conditions
    * Load cities and areas data from S3
    * Parse and index cities data
    * Load diseases data from S3
    * Add diseases to cities with high risk to them
    * Parse relations between risk groups and cities with high risk to diseases
    * Load cities data from S3
    * Create polluted cities based on environmental values
    * Create polluted cities based on target values
    * Parse relations between polluted cities and risk groups
    * Upload the indexed cities, polluted cities and risk group relations to the graph.