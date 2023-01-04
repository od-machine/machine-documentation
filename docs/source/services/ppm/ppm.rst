PPM
===
A product to provide health insurance policyholders with individualized recommendations for diagnostic testing, promoting preventive and personalized health.

.. image:: ppm_flow.png


Prerequisites
~~~~~~~~~~~~~

**Medical recommendations data should be indexed onto the neo4j graph.**

.. image:: ppm_graph.png

* Data for the recommendations was taken from several sources, the majority came from the MOH 2022 recommendation document.

* In addition to the recommendations, there are links to articles and links that provide further information.

* Every recommendation is tailored to specific groups of the population based on a number of factors, such as their age (minimum/maximum), gender, biochemical variables, and other factors.



.. toctree::
   :maxdepth: 3
   :caption: APIs
   
   index_patient_api
   update_recommendations_api
