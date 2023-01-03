Cities
======

.. function:: remove_city_condition

This function removes the nodes with the label "Condition" and the property "Name_By_Questionnaire" equal to "Remove_City" from the graph database.
Input: None
Output: None (the function only removes nodes from the graph database and does not return anything)

.. function:: get_df_from_s3

This function reads a CSV file from an S3 bucket and returns the data as a Pandas DataFrame.
Input:
path (string): path to the CSV file in S3 (e.g. 's3://my-bucket/data/file.csv')
Output:
df (Pandas DataFrame): DataFrame containing the data read from the CSV file

.. function:: connect_cities_and_areas

    This function creates a list of dictionaries representing the relationships between cities and areas.
    Input:
    cities_and_areas_df (Pandas DataFrame): DataFrame with columns 'YISHUV_STA' and 'SEMEL_YISH' representing the cities and areas, respectively
    Output:
    cities_and_areas_list (list of dictionaries): Each dictionary in the list represents a relationship between a city and an area, with the keys 'from', 'to', and 'rel_type' (e.g. {'from': 'city1', 'to': 'area1', 'rel_type': 'AREA_IN'})§




.. function:: parse_index_stats_areas

    Create list of statistical areas to create nodes.

    :param cities_and_areas_df: data frame with cities and area data
    :type cities_and_areas_df: pandas.core.frame.DataFrame
    :return: list of dictionaries of the areas
    :rtype: list

.. function:: parse_index_cities

    Create list of cities to create nodes.

    :param cities_and_areas_df: data frame with cities and area data
    :type cities_and_areas_df: pandas.core.frame.DataFrame
    :return: dictionary of dictionaries of all cities and their details, list of dictionaries of the cities
    :rtype: dict, list

.. function:: upload_geographic_data

    Upload all cities, statistical areas, and relations to risk groups to the graph.

    :param cities_list: to create City nodes
    :type cities_list: list
    :param poll_cities_risk_group: to create relations to air pollution risk groups
    :type poll_cities_risk_group: pandas.core.frame.DataFrame
    :param diseases_cities_and_risk_groups_list: to create relations to high risk to diseases risk groups
    :type diseases_cities_and_risk_groups_list: list



.. function:: load_diseases_df_from_s3

    This function retrieves a data frame containing data on diseases in cities from an S3 bucket, and performs some adjustments on the data. It renames the columns and converts the city id column to a numerical data type. The function returns the resulting data frame.

    Get the diseases data frame from s3.

    change columns names, change city id column to number
    :return disease_df: the data frame after the adjustments


.. function:: load_cities_df_from_s3

    This function loads data frames containing data on cities from an S3 bucket, and stores them in a dictionary. It also retrieves a dictionary of thresholds from the S3 bucket. The function returns the dictionary of data frames and the thresholds dictionary.

    Load the cities data frames from s3 to dict and load the thresholds dict from s3
    :return cities_df_dict: dictionary of data farme, when the keys are years
    :return air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)


.. function:: add_polluted_city_to_conditions

    This function takes in a dictionary of city data, a data frame containing air pollution data for cities, and a dictionary of thresholds for air pollution levels. It adds a boolean value "Polluted_City" to the city data dictionary for each city that has air pollution levels above the environment value in the thresholds dictionary. The function returns the updated city data dictionary.

    Parse the polluted cities that higher than environment value
    
    :param cities_dict: dictionary of dictionaries - all cities and their details
    :param df: air pollution data per cities data frame
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :return cities_dict: dictionary of all cities and their details - updated with polluted cities

.. function:: create_polluted_city_by_env_val

    This function takes in a dictionary of city data, a dictionary of data frames containing data on cities, and a dictionary of thresholds for air pollution levels. It checks for cities that have air pollution levels above the environment value in the thresholds dictionary, and adds a boolean value "Polluted_City" to the city data dictionary for each such city. The function returns the updated city data dictionary.

    Check for polluted city that higher than environment value

    :param cities_dict: dictionary of dictionaries - all cities and their details
    :param cities_df_dict: dictionary of data farme, when the keys are years
    :param air_pollution_thresholds: thresholds dict (env val and target val for each pollutant)
    :return cities_dict: dictionary of all cities and their details - updated with polluted cities


.. function:: get_disease_df_by_year

    This function takes in a data frame containing data on diseases in cities and a year, and returns a data frame with data for the given year.

    :param df: data frame of diseases in cities
    :param year: year to filter the data
    :return df: data frame after filtering the year


.. function:: calculate_diseases_ratio

    This function takes in a data frame containing data on diseases in cities, and calculates the ratio of each disease to the total number of people in the city. The function returns a data frame with the calculated ratios.

    :param df: data frame of diseases in cities
    :return df: data frame with ratio of each disease to the total number of people in the city


.. function:: sort_cities_by_diseases

    This function takes in a data frame containing data on diseases in cities and a year, and sorts the cities by the sum of their disease ratios for the given year. The function returns a list of city ids sorted in this manner.

    :param df: data frame of diseases in cities
    :param year: year to filter the data
    :return list: list of city ids sorted by sum of disease ratios


.. function:: create_report

    This function takes in a list of city ids sorted by disease ratios, a dictionary of city data, and a year. It creates a report detailing the top 10 cities with the highest disease ratios for the given year. The report includes the city id, name, and disease ratios for each city. The function returns the report as a string.

    :param sorted_cities: list of city ids sorted by disease ratios
    :param cities_dict: dictionary of city data
    :param year: year to include in the report
    :return str: report detailing top 10 cities with highest disease ratios
