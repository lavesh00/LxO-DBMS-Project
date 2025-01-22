from sql_agent import SQLAgent
from nosql_agent import NoSQLAgent

class ArbitrationAgent:
    def __init__(self, data):
        self.data = data

    def is_structured(self):
        """ Check if data is structured based on required keys """
        required_keys = ["name", "age", "department"]
        return all(key in self.data for key in required_keys)

    def route_to_sql_or_nosql(self):
        """ Decide where to store data: Oracle (SQL) or MongoDB (NoSQL) """
        if self.is_structured():
            sql_agent = SQLAgent()
            return sql_agent.insert_data(self.data)
        else:
            nosql_agent = NoSQLAgent()
            return nosql_agent.insert_data(self.data)
