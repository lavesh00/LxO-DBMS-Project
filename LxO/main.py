import os
import cx_Oracle
from arbitration_agent import ArbitrationAgent
from get_connection import get_oracle_connection, get_mongo_connection

def check_oracle_client():
    """Check if Oracle Instant Client is installed."""
    if "ORACLE_HOME" not in os.environ:
        print("Oracle Instant Client is not installed or not configured. Please install it first.")
        return False
    return True

def prompt_user_for_table_creation(connection):
    """Prompt the user to create a table dynamically in Oracle."""
    table_name = input("Enter the name of the table to create: ")
    num_columns = int(input("Enter the number of attributes (columns) for the table: "))
    columns = []

    for i in range(num_columns):
        column_name = input(f"Enter the name of column {i + 1}: ")
        data_type = input(f"Enter the data type for column {column_name} (e.g., VARCHAR2(50), NUMBER, DATE): ")
        columns.append(f"{column_name} {data_type}")

    create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"

    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print(f"Table '{table_name}' created successfully!")
    except cx_Oracle.Error as e:
        print(f"Error creating table: {e}")

    return table_name  # Return the name of the table for further operations

def main():
    # Check for Oracle Client
    if not check_oracle_client():
        return

    # Get Oracle and MongoDB connection details
    oracle_user = input("Enter Oracle username: ")
    oracle_password = input("Enter Oracle password: ")
    oracle_host = input("Enter Oracle host (e.g., localhost): ")
    oracle_port = input("Enter Oracle port (e.g., 1521): ")
    oracle_service = input("Enter Oracle service name (e.g., xe): ")

    mongo_uri = input("Enter MongoDB URI (e.g., mongodb://localhost:27017/): ")
    mongo_db_name = input("Enter MongoDB database name: ")

    # Establish connections
    oracle_connection = get_oracle_connection(oracle_user, oracle_password, oracle_host, oracle_port, oracle_service)
    mongo_collection = get_mongo_connection(mongo_uri, mongo_db_name)

    # Allow user to create a table in Oracle
    table_name = prompt_user_for_table_creation(oracle_connection)

    # Prompt user for data
    print("Enter data for insertion (structured data will go to Oracle, unstructured to MongoDB):")
    data = {}
    while True:
        key = input("Enter key (or 'done' to finish): ")
        if key.lower() == "done":
            break
        value = input(f"Enter value for {key}: ")
        data[key] = value

    # Route data
    arbitration_agent = ArbitrationAgent(data)
    result = arbitration_agent.route_to_sql_or_nosql(oracle_connection, mongo_collection, table_name)

    print(result)

if __name__ == "__main__":
    main()
