.. function:: upload_conditions(recommendations_df) -> None:
    
    Call function to create all conditions nodes and relationships.
    
    1. Calls ׳get_risk_group_age_ranges׳ to get a dataframe of age ranges from the riskgroups
    2. Calls ׳get_age_range_data_from_risk_groups׳ to get 4 variables:
        list of age-ranges-conditions-ids
        dictionary of {age-range-condition-id: [risk=group-ids]}
        list of tuples: (min_age, max_age, conditionId)
        list of dictionaries of age-ranges conditions
    3. Create Age Ranges Condition nodes
    4. Create the relationship between the Age Ranges Condition nodes and the Risk Group nodes
    5. Gets a df  of all the Conditions from the excel
    6. Add_conditions_to_postgresql and df with odm_id for each general condition_name
    7. Merge above 2 df and convert df  to list 
    8. Create the Condition nodes
    9. Create the relationship between the Condition nodes and the Risk Group nodes
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame


.. function:: get_risk_group_age_ranges() -> DataFrame:
    
    Execute a cypher query to get the risk-groups Id, maximum-age, minimum-age.

    :return: risk groups DataFrame.


.. function:: get_age_range_data_from_risk_groups(risk_group_age_ranges) -> (list, dictionary, list, dictionary, ):

    1. Add a condition id and delete rows where there is no Min_Age and Max_Age.
    
    2. Create a reduced dataframe without duplicate rows (same Min and Max Age).
    
    3. For each risk group (before removing duplicates), find the unique condition ID that matches it, then update a global dictionary with the risk group ID (key is the (unique) condition ID)
    
    4. Cut the reduced dataframe and leave only the Condition_Id, Type, Min_Age, Max_Age.
    
    5. For each condition, update a list of tuples containing (Min_Age, Max_Age, Condition_Id).

    :param risk_group_age_ranges: all recommendations.
    :type risk_group_age_ranges: DataFrame
    :return: (conditions_ids_list - list of age-ranges-conditions-ids, unique_age_range_risk_group_dict - dictionary of {age-range-condition-id: [risk=group-ids]}, age_range_list - list of tuples: (min_age, max_age, conditionId), age_ranges_list - list of dictionaries of age-ranges conditions)


.. function:: find_row_with_values(df, min, max) -> DataFrame:
    
    Finds in a given DataFrame a row with 'Min_Age' and 'Max_Age' equals to given parameters

    :param df:
    :type df: DataFrame
    :param min:
    :type min: int
    :param max:
    :type max: int
    :return: the required row from the given DataFrame.


.. function:: create_conditions_df(Condition_Id, recommendations_df) -> DataFrame:
    
    Extract general conditions DataFrame.

    1. call ׳conversion_of_column_to_lists_by_comma_and_then_to_one_list׳.
    2. add condition id

    :param Condition_Id: all conditions ids.
    :type Condition_Id: list
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :return: conditions DataFrame.


.. function:: conversion_of_column_to_lists_by_comma_and_then_to_one_list(column_name, new_colume, recommendations_df) -> DataFrame:
    
    1. Add the gender to the conditions
    2. Conversion to lists and strip the whitespace
    3. Convert from lists to list

    :param column_name:
    :type column_name: str
    :param new_colume: 
    :type new_colume: str
    :param recommendations_df: all recommendation.
    :type recommendations_df: DataFrame
    :return: the DataFrame after adjustments.


.. function:: remove_origin_conditions(condition_df) -> DataFrame:
    
    Remove from the condition_df conditions that contains an Origin condition.

    :param conditions_df: dataframe with columns [Type, Condition_Name, Name_By_Questionnaire, Condition_Id].
    :type conditions_df: DataFrame
    :return: the input DataFrame without rows where the value in the 'Condition_Name' column is part of the origin dictionary.


.. function:: create_origins_df() -> DataFrame:
    
    Create a dataframe for the origin nodes creation in the graph.

    :param conditions_df: dataframe with columns [Type, Condition_Name, Name_By_Questionnaire, Condition_Id].
    :type conditions_df: DataFrame
    :return: origins DataFrame that contains [Type, Condition_Name, Name_By_Questionnaire, Hebrew_Name, Condition_Id].


.. function:: create_odm_id(nodes_list, table_name, main_attribute_name, column_name, node_odm_id_name) -> dictionary:
    
    Create odm_id for nodes and upload to postgresql.

    1. Call ׳add_nodes_to_postgresql׳ to uploads the nodes to the specific table in postgresql where it gets an odm_id.
    2. Add th odm_id to the node as a new column in the df.

    :param nodes_list: the nodes we want to get odm_id for them.
    :type nodes_list: DataFrame
    :param table_name: the postgresql table name.
    :type table_name: str
    :param main_attribute_name: the attribute that corresponds to the name of the node ('Condition_Name'/'Origin_Name').
    :type main_attribute_name: str
    :param column_name: the name of the column (other than odm_id) in the postgresql table.
    :type column_name: str
    :param node_odm_id_name: the name of the odm_id for the node ('Condition_Odm_Id'/'Origin_Odm_Id').
    :type node_odm_id_name: str
    :return: the nodes with the odm_id


.. function:: add_nodes_to_postgresql(nodes_df, table_name, main_attribute_name, column_name, node_odm_id_name) -> DataFrame:
    
    Add nodes to the postgresql table where a sequence gives every id an odm_id depending on the table.

    :param node_df: the data to insert to postgresql table.
    :type node_df: DataFrame
    :param table_name: 'ppmconditionsseq'/'ppmoriginsseq'.
    :type table_name: str
    :param main_attribute_name: 'Condition_Name'/'Origin_Name'.
    :type main_attribute_name: str
    :param column_name: 'condition_name'/'origin_name'.
    :type column_name: str 
    :param node_odm_id_name: 'Condition_Odm_Id'/'Origin_Odm_Id'.
    :type node_odm_id_name: str
    :return: dataframe with odm_id and node_name

.. function:: create_age_range_risk_groups_relationships(unique_age_range_risk_group_dict) -> None:

    Create risk groups and age conditions relations.
    
    1. Call ׳create_age_range_risk_groups_relationships_list׳ to create relations list.
    2. Create the relationships in the neo4j graph.

    :param unique_age_range_risk_group_dict:
    :type unique_age_range_risk_group_dict: dictionary


.. function:: create_age_range_risk_groups_relationships_list(unique_age_range_risk_group_dict) -> list:

    Create a list of dictionaries for creating relationships.
    
    For each 'Condition_Id' from the unique Age Range dictionary, iterate over the list of 'Risk_Group_Id' and insert to a dictionary in the desired format.

    :param unique_age_range_risk_group_dict: dictionary from the form {age-range-conditionId : [condition ids]}
    :type unique_age_range_risk_group_dict: dictionary
    :return: list of relations dictionaries.


.. function:: create_nodes_risk_groups_relationships(nodes_dict, recommendations_df, label, node_name, node_id_name) -> None:

    Create relationships between a given type of node to risk group nodes. 
    
    1. Call ׳create_conditions_risk_groups_relationships_list׳ to generates a list of relationships.
    2. Create the relationships in the neo4j graph.

    :param nodes_dict: the nodes properties.
    :type nodes_dict: dictionary
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :param label: the source node's label from (Condition/Origin)
    :type label: str
    :param node_name: the property name of the given label (Condition_Name/Origin_Name).
    :type node_name: str
    :param node_id_name: the id property naem of the given label (Condition_Id/Origin_Odm_Id).
    :type node_id_name: str


.. function:: create_conditions_risk_groups_relationships_list(Conditions, recommendations_df, node_name, node_id_name) -> list:

    Create a list of dictionaries for creating relationships.

    Go over the conditions in parallel with the conditions lists and check which conditions appear in which list. Accordingly connect Condition_Id to Risk_Group_Id.
    
    :param Conditions: the nodes properties
    :type Conditions: DataFrame
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :param node_name: the property name of the given label (Condition_Name/Origin_Name).
    :type node_name: str
    :param node_id_name: the id property naem of the given label (Condition_Id/Origin_Odm_Id).
    :type node_id_name: str
    :return: list of relations dictionaries.
