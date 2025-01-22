from flask import Flask, request, jsonify
from arbitration_agent import ArbitrationAgent

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    arbitration_agent = ArbitrationAgent(data)
    
    result = arbitration_agent.route_to_sql_or_nosql()  # Decide and insert data
    return jsonify(result), 200

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Fetch data from Oracle (SQL)
        from sql_agent import SQLAgent
        sql_agent = SQLAgent()
        oracle_data = sql_agent.fetch_data()

        # Fetch data from MongoDB (NoSQL)
        from nosql_agent import NoSQLAgent
        nosql_agent = NoSQLAgent()
        mongo_data = nosql_agent.fetch_data()

        return jsonify({
            "oracle_data": oracle_data,
            "mongo_data": mongo_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
