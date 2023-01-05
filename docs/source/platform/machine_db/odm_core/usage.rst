Usage
=====

neo4j handler
~~~~~~~~~~~~~

Connect to neo4j desktop (localhost):
+++++++++++++++++++++++++++++++++++++

.. sourcecode:: python

    # import Neo4jHandler class
    from odmcore.neo4j.neo4j_handler import Neo4jHandler
    # connect to localhost example
    graphDB = Neo4jHandler(neo4j_lb = 'localhost', neo4j_db = 'neo4j', 
                    neo4j_user = 'neo4j', neo4j_password = '****')


Connect to neo4j servers:
+++++++++++++++++++++++++

.. sourcecode:: python

    # import Neo4jHandler class
    from odmcore.neo4j.neo4j_handler import Neo4jHandler
    # fetch global os environments
    access_key = os.environ["ACCESS_KEY"] 
    secret_access_key = os.environ["SECRET_ACCESS_KEY"]
    secret_name= os.environ['NEO4J_SECRET']
    neo4j_lb = os.environ['NEO4J_LB']
    neo4j_db = os.environ['NEO4J_DB']
    # connect to neo4j remote server
    graphDB = Neo4jHandler(neo4j_lb = neo4j_lb, neo4j_db = neo4j_db, secret_name = secret_name, aws_access_key = access_key, aws_secret_access_key = secret_access_key)

Now, you can use every function in neo4j class.
For example you can fetch data from the graph: 

.. sourcecode:: python

    graphDB.get_data_from_graph('MATCH (n:DO) RETURN n.DO_Id LIMIT 1')
    graphDB.create_node("A",{"name": "aaa"})


S3 buckets handler
~~~~~~~~~~~~~~~~~~

Connect to S3 bucket:
+++++++++++++++++++++

.. sourcecode:: python

    #import S3Handler class
    from odmcore.s3.s3_handler import S3Handler
    # fetch global os environments
    access_key = os.environ["ACCESS_KEY"] 
    secret_access_key = os.environ["SECRET_ACCESS_KEY"]
    bucket_name = os.environ["BUCKET_NAME"]
    buckets3 = S3Handler(bucket_name, access_key, secret_access_key)

Now, you can perform various actions on your S3 buckets.
Here is an example of getting a list of all files in a folder on Nuete bucket:

.. sourcecode:: python

    s3_path = 'odb-data/Drugbank/'
    files = buckets3.list_files_in_dir(s3_path)
    print(files)


Postgres handler
~~~~~~~~~~~~~~~~

Connect to postgres localhost:
++++++++++++++++++++++++++++++

In order to test your code on localhost you have to install 
postgres on your machine.

`Here <https://medium.com/@viviennediegoencarnacion/getting-started-with-postgresql-on-mac-e6a5f48ee399>`_
you can find a guide for postgres installation on mac.

NOTE : It is important to define a new role for your username and password.

After postgres is installed you can use pg-admin to connect to the local server 
as described `here <https://www.postgresqltutorial.com/postgresql-getting-started/connect-to-postgresql-database/>`_.

Build an instance of the PostgresHandler class in order to connect to 
your local postgres:

.. sourcecode:: python

    #connect to local postgres database
    postgres = PostgresHandler(postgres_hostname = 'localhost', postgres_db = 'postgres', postgres_user='postgres', postgres_password='****')

Connect to postgres remote database:
++++++++++++++++++++++++++++++++++++

.. sourcecode:: python

    #import PostgresHandler
    from odmcore.postgres.postgres_handler import PostgresHandler
    # fetch global os environments
    access_key = os.environ["ACCESS_KEY"] 
    secret_access_key = os.environ["SECRET_ACCESS_KEY"]
    secret_name = os.environ['POSTGRES_SECRET']
    postgres_hostname = os.environ['POSTGRES_HOST']
    postgres_db = os.environ['POSTGRES_DB']
    secret_region_name = os.environ['REGION']
    #connect to postgres database
    postgres = PostgresHandler(postgres_hostname, postgres_db, access_key, secret_access_key, secret_region_name, secret_name)

Now, you can use the postgres handler to perform 
different actions on your postgres server.
For example: 

.. sourcecode:: python

    query = 'select * from score'
    res = postgres.get_data_from_sql(query)
    print(res)


Logs handler
~~~~~~~~~~~~

Write logs to the console:
++++++++++++++++++++++++++

.. sourcecode:: python

    from odmcore.logs.logs_handler import LoggerWrapperDB
    # When write_log_file=False (default) the logs will be wrote into the console only
    # When write_log_file=True the logs will be wrote into a file also
    logger = LoggerWrapperDB()
    logger.start()

Write logs to a json file:
++++++++++++++++++++++++++

.. sourcecode:: python

    from odmcore.logs.logs_handler import LoggerWrapperDB
    # When write_log_file=False (default) the logs will be wrote into the console only
    # When write_log_file=True the logs will be wrote into a file also
    logger = LoggerWrapperDB(write_log_file=True)
    logger.start()


In order to use functions that connect with 
the graph you should send the graph object to the
logs definition.

For example:

.. sourcecode:: python

    from odmcore.logs.logs_handler import LoggerWrapperDB
    from odmcore.neo4j.neo4j_handler import Neo4jHandler
    # Build graph object
    neo4j = Neo4jHandler(neo4j_lb = 'localhost', neo4j_db = 'neo4j', 
                        neo4j_user = 'neo4j', neo4j_password = '****')
    # Send the graph object to the logs definition                 
    logger = LoggerWrapperDB(graph_db=neo4j)
    logger.write_rels_amounts('Reaction', 'GO', 'compartment')
    logger.write_nodes_amounts('Pathway')

Read more about logs `here <https://docs.google.com/document/d/1bY_5dXihvwd5an1SAw0LB0GuO1qeGTdqsJvy0gPGFYk/edit?usp=sharing>`_


Arango-db handler
~~~~~~~~~~~~~~~~~

Connect to Arango localhost:
++++++++++++++++++++++++++++

.. sourcecode:: python

    # import ArangoDBHandler class
    from odmcore.arango.arangoDB_handler import ArangoDBHandler
    # connect to localhost example
    arangoDB = ArangoDBHandler(db_name="test", host="http://localhost:8529", username='****', password='****')

For Arango remote connection the host address should be replaced to the remote one.


MetrictHandler
~~~~~~~~~~~~~~

Init the metric module on Flask api program:
++++++++++++++++++++++++++++++++++++++++++++

.. sourcecode:: python

    from app import create_app
    # import MetricsHandler class
    from odmcore.metrics.metrics_handler import MetricsHandler

    app = create_app()

    if __name__ == '__main__':
        # init the Metric module
        MetricsHandler(app, 'Sync - Micro service')
        app.run(host='0.0.0.0', debug=True, port=80)

init the metric module on non-api program:
++++++++++++++++++++++++++++++++++++++++++

.. sourcecode:: python
    # import MetricsHandler class
    from odmcore.metrics.metrics_handler import MetricsHandler

    def main():
        # init the Metric module
        MetricsHandler('Test-app', env='dev')


- Read more about the MetricsHandler class `here <https://docs.google.com/presentation/d/1jhVOj58B4AdbFau-PKiU2aMVVAtYEhe21ZC4q_m1BDo/edit#slide=id.g107285708c1_0_0>`_

- Read more about Prometheus `here <https://docs.google.com/document/d/1_eZkO1pG1j6u6X395UH1r8hol233h-LD7_DsZgZLf4w/edit#heading=h.uqbh38ruihbz>`_


