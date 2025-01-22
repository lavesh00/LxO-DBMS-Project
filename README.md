# LxO-DBMS-Project
# Multi-Agent Database Query Arbitration System

This project implements a Multi-Agent System for SQL-NoSQL Query Arbitration. The system dynamically decides whether to use Oracle Database (SQL) or MongoDB (NoSQL) for storing and retrieving data based on the structure of the input data.

## Features

- **Oracle Database Integration**: Support for creating tables and inserting structured data.
- **MongoDB Integration**: Support for inserting unstructured data into MongoDB.
- **Dynamic Decision Making**: Automatically determines whether data is structured or unstructured and routes it to the appropriate database.
- **EXE Distribution**: The application is distributed as an executable for ease of use.

## Prerequisites

### Oracle Database

- Oracle Instant Client must be downloaded and placed in the project directory under `instantclient_21_3`.
- Ensure Oracle Database is installed and accessible.

### MongoDB

- MongoDB must be installed and running on the specified host.

### Python

- Python 3.7 or later

## Directory Structure

```
project/
├── main.py
├── instantclient_21_3/  # Oracle Instant Client files
│   ├── oci.dll
│   ├── ...
├── requirements.txt
└── dist/                # Output folder for the EXE
```

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/multi-agent-database-arbitration.git
   cd multi-agent-database-arbitration
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add Oracle Instant Client:

   - Download Oracle Instant Client from [Oracle's website](https://www.oracle.com/database/technologies/instant-client.html).
   - Place the downloaded files in the `instantclient_21_3` folder.

4. Configure Environment Variables (Optional):

   - Add the path to the `instantclient_21_3` directory to the `PATH` environment variable.

## Usage

### Run the Application

To run the application:

```bash
python main.py
```

### Generate the EXE

To generate a standalone executable:

```bash
pyinstaller --onefile main.py
```

The executable will be available in the `dist/` directory.

### Workflow

1. The program checks for the Oracle client.
2. Users are prompted to provide:
   - Oracle credentials (username, password, host, port, and service name).
   - MongoDB connection string and collection details.
3. Users specify table attributes and create tables in Oracle or insert data into MongoDB.

## Examples

### Creating a Table in Oracle

When prompted, provide table details:

```
Enter the table name: employees
Enter columns in the format 'col1 datatype, col2 datatype': id NUMBER, name VARCHAR2(50), age NUMBER
```

### Inserting Data into MongoDB

When prompted, provide JSON data:

```
Enter JSON data to insert into MongoDB (e.g., {"key": "value"}):
{"name": "John Doe", "age": 30, "department": "HR"}
```

## Troubleshooting

- **Oracle Client Not Found**: Ensure `instantclient_21_3` is present and initialized correctly.
- **MongoDB Connection Error**: Verify that MongoDB is running and accessible.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Developed by Lavesh Patil.

