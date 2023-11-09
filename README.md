# AirtoNeo
Python code to transfer data from Airtable to Neo4j.

# Instantiating the class
The AirtoNeo class expects two dictionaries as input in the form:
neocreds = {'uri':Neo4j URI, 'user': Neo4j database user, 'password': Neo4j database password}
aircreds = {'token': Airtable token,'baseID': Airtable base ID, 'tableID': Airtable table ID}

When you create an instance of the class, it will automatically connect to both your Airtable table and your Neo4j database.

```air2neo = AirtoNeo(neocreds,aircreds)```

# Accessing the Airtable

You can access the Airtable object as an attribute of the class.

```table = air2neo.Airtable```

# Writing Data to Neo4j

You can use the AirtoNeo instance to run cypher write queries onto your database.
The run_cypher() method expects a dictionary of the form {cypher_query, dataframe}, where the cypher_query is a string and the dataframe is the data to run the query on.
The dataframe value can be a list of dataframes, if you want to run the same query on multiple dataframes.
If you want to run a cypher query that doesn't run on a dataframe, then have the value of the dictionary for that query key to None.

```airtoneo.run_cypher(load_queries,verbose=True)```
