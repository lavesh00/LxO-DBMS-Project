import cx_Oracle
from get_connection import get_oracle_connection

class SQLAgent:
    def __init__(self):
        self.connection = get_oracle_connection()

    def insert_data(self, data):
        """ Insert structured data into Oracle """
        try:
            cursor = self.connection.cursor()

            # Ensure that emp_id_seq.NEXTVAL is used to auto-generate the ID
            query = """
            INSERT INTO employees (id, name, age, department)
            VALUES (emp_id_seq.NEXTVAL, :name, :age, :department)
            """
            cursor.execute(query, {"name": data['name'], "age": data['age'], "department": data['department']})
            self.connection.commit()
            cursor.close()

            return {"message": "Data inserted into Oracle successfully!"}

        except cx_Oracle.Error as e:
            error, = e.args
            print(f"Oracle Error: {error.message}")  # Log the error message to the console
            return {"error": f"Oracle Error: {error.message}"}

        except Exception as e:
            print(f"Unexpected Error: {str(e)}")  # Log any other errors to the console
            return {"error": f"Unexpected Error: {str(e)}"}

    def fetch_data(self):
        """ Fetch data from Oracle """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM employees")
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception as e:
            return {"error": str(e)}
