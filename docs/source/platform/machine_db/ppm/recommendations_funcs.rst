Functions
---------

:kbd:`Recommendations:`

.. function:: upload_recommendations() -> DataFrame:
    
    Call function to create all recommendations nodes and relationships.
    
    :returns: The recommendations DataFrame.
    

.. function:: create_recommendations_df() -> DataFrame:

    Read the recommendations from s3.
    
    Delete empty columns.
    
    Send the data frame to `create_recommendations_df_parser` to make more adjustments. 
    
    :returns: The recommendations DataFrame after adjustments.


.. function:: create_recommendations_df_parser(recommendations_df) -> DataFrame:
    
    Remove the spaces at the end and beginning of the columns name.
    
    Replace the middle spaces with "_".
    
    Add unique id for each screening test(recommendation) and risk group.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :returns: The recommendations DataFrame after adjustments.


.. function:: create_recommendations(recommendations_df) -> None:
    
    Call `add_recomendations_to_postgresql` to add the recommendations to postgresql.

    Add the odm_id to the *recommendations_df*.
    
    Call `create_recommendations_nodes_list` and then create the recommendations nodes in neo4j graph.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame


.. function:: add_recomendations_to_postgresql(recommendations_df) -> DataFrame:

    Add the recommendation names from the *Recommendation_Names* column if it not found in *ppmrecommendationsseq* table in postgresql.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :returns: recomendations_names_df: DataFrame of the recommendations names and their odm ids


.. function:: create_recommendations_nodes_list(recommendations_df) -> DataFrame:
    
    Leave only the relevant columns from *recommendations_df*.
    
    Add PPM_VERSION to the DataFrame.
    
    Transfer to a dictionary.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :returns: The DataFrame as a dictionary.


:kbd:`Risk groups:`


.. function:: create_risk_groups(recommendations_df) -> None:

    call ׳create_risk_groups_nodes_list׳ to create list of risk groups.

    Create the risk groups nodes in the neo4j graph.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame

.. function:: create_risk_groups_nodes_list(recommendations_df) -> dictionary:

    Cut the main data frame and leave only the 'Risk_Group_Id', 'Gender', 'Min_Age', 'Max_Age', 'Risk_Factors' columns.
    
    Delete duplicate values, add PPM_VERSION and Database.
    
    Convert to dictionary and return it

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :returns: The risk groups dictionary.


.. function:: create_tests_risk_groups_relationships(recommendations_df) -> None:

    Call ׳create_tests_risk_groups_relationships_list׳ to create list of recommendations and risk groups relations.

    Create the relationships in neo4j graph.

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame


.. function:: create_tests_risk_groups_relationships_list(recommendations_df) -> dictionary:

    Create DataFrame of risk groups and related recommendation tests.
    
    Convert to a dictionary and return it.

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :returns: The risk groups and recommendations relations dictionary.


:kbd:`References:`


.. function:: create_reference_groups(recommendations_df) -> None:
    
    Iterate i, for each i in range (1,5):

        Call ׳create_reference_df_and_list׳ to create a list of the i'th reference.

        Create the references nodes in the neo4j graph.

        Call ׳create_reference_risk_groups_relationships׳ to create the i'th references and risk groups relations.
    
    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame



.. function:: create_reference_df_and_list(ref_index, recommendations_df) -> (Database, dictionary)
    
    Create Database only from the reference[ref_index] and reference link[ref_index].
    
    Delete columns with no references, , add PPM_VERSION and Database.
    
    Return it as a Database and as a dictionary.

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :param ref_index: reference number (1-4).
    :type ref_index: int
    :return: reference Database, reference dictionary


.. function:: create_reference_risk_groups_relationships(ref_df, recommendations_df) -> None:

    Call ׳create_reference_risk_groups_relationships_list׳ to create a list of references and risk groups relations.

    Create the relations in the neo4j graph.

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :param ref_df: all recommendations.
    :type ref_df: DataFrame


.. function:: create_reference_risk_groups_relationships_list(ref_df, recommendations) -> dictionary:

    Create data frame of risk groups and related references

    Convert to a dictionary and return it

    :param recommendations_df: all recommendations.
    :type recommendations_df: DataFrame
    :param ref_df: all recommendations.
    :type ref_df: DataFrame
    :return: references and risk groups relations dictionary 
