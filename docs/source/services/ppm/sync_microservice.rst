* *update recommendations* API

API to index the patient's questionaire details to the ArangoDB.


**run example**:

url: ``http://<NETWORK>:<PORT>/api/v1/ppm/update_patients_conditions_and_recommendations``


**actions**:

1. Read the conditions from neo4j and the patients from arangoDB.
2. Match the patients and appropriate conditions.
3. Read the recommendations from neo4j according to the patient's conditions.
4. Read the summary about the patients from arango db and translate it.
5. Update or add to the arangoDB recommendations collection all the recommendations that readed from neo4j.
6. Update or add to the arangoDB edges collection the relations between the patients and the recommendations.

