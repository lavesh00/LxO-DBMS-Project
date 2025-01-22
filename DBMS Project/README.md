# DBMS Project: SQL-NoSQL Query Arbitration

## Description:
This project implements a system that arbitrates between SQL (Oracle) and NoSQL (MongoDB) based on the structure of the data being inserted. If the data is structured, it will be inserted into Oracle, and if it is unstructured, it will be inserted into MongoDB.

## Setup:

1. **Create a Virtual Environment**:
    - In the project directory, run the following command to create a virtual environment:
      ```
      python -m venv env
      ```

2. **Activate the Virtual Environment**:
    - On Windows:
      ```
      .\env\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source env/bin/activate
      ```

3. **Install Dependencies**:
    - Run the following command to install the necessary libraries:
      ```
      pip install -r requirements.txt
      ```

4. **Configure Database Connections**:
    - Set up the Oracle and MongoDB connection details in the `get_connection.py` file.

5. **Run the Flask Application**:
    - Start the Flask application by running the following command:
      ```
      python script.py
      ```

6. **Testing the System**:
    - Send a POST request to `/insert` with JSON data, either structured or unstructured.
    - The system will insert the data into the appropriate database (Oracle or MongoDB).

7. **Fetching Data**:
    - Send a GET request to `/fetch` to retrieve data from both Oracle and MongoDB.

## License:
This project is open-source and licensed under the MIT License.
