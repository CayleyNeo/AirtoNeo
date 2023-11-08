class AirtoNeo:
    
    def __init__(self, Neo4j_credentials, Airtable_credentials):
        
        '''
        Expects a dictionary of Neo4j credentials in the form {'uri':Neo4j URI, 'user': Neo4j database user, 'password': Neo4j database password}
        Also expects a dictionary of Airtable credentials in the form {'token': Airtable token,'baseID': Airtable base ID, 'tableID': Airtable table ID}
        '''
        
        # Neo4j Credentials
        self.__Neo4jURI = Neo4j_credentials['uri']
        self.__Neo4jusername = Neo4j_credentials['user']
        self.__Neo4jpassword = Neo4j_credentials['password']
        
        # Airtable Credentials
        self.__AirtableToken = Airtable_credentials['token']
        self.__AirtableBaseId = Airtable_credentials['baseID']
        self.__AirtableTableId = Airtable_credentials['tableID']
        
        
        # Setting up the Airtable connection or, if failed, returning the error to the client
        try:
            # Connecting to the database
            self.AirtableConnection = Api(self.__AirtableToken)
            print(f'You are connected to Airtable as user: {self.AirtableConnection.whoami()}')
            self.Airtable = atconnect.table(self.__AirtableBaseId,self.__AirtableTableId)
        except Exception as e:
            print(f'Airtable connection failed with error: {e}.')
            self.Airtable = None
            self.Airtable = None
            
        # Setting up the Neo4j connection or, if failed, returning the error to the client
        try:    
            self.Neo4jGraph = Neo4jInstance(self.__Neo4jURI, self.__Neo4jusername, self.__Neo4jpassword)
            print(f'You are connected to Neo4j.')
        except Exception as e:
            print(f'Neo4j connection failed with error: {e}')
            self.Neo4jGraph = None
    
    # Loading the initial data
    
    def run_cypher(self,load_dict:dict,verbose=False):
        '''
        This function loads initial data from Airtable to Neo4j.
        It expects a dictionary in the form of {cypher_query:dataframe} where the cypher_query is a string.
        It will run the cypher query on each dataframe.
        If you want to run the same cypher query on multiple dataframes, change the format to {cypher_query:[dataframes]}
        If you want to see a print statement for each cypher statement, set verbose = True.
        '''
        for query in load_dict:
            if isinstance(load_dict[query],list):
                for df in load_dict[query]:
                    result = self.Neo4jGraph.execute_write_query_with_data(query,df)
                    if verbose:
                        print(result)
            elif isinstance(load_dict[query],pd.DataFrame):
                result = self.Neo4jGraph.execute_write_query_with_data(query,load_dict[query])
                if verbose:
                    print(result)    