from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
CORS(app)

@app.route('/deforestation-data', methods=['GET'])
def get_deforestation_data():
    # Replace this with actual data retrieval logic
    data = {
        'region': 'Amazon Rainforest',
        'deforestation_rate': 0.05,  # Example deforestation rate
        'year': 2021
    }
    return jsonify(data)

@app.route('/climate-change-data', methods=['GET'])
def get_climate_change_data():
    # Replace this with actual data retrieval logic
    data = {
        'average_temperature': 14.6,  # Example average temperature
        'co2_concentration': 412.5,  # Example CO2 concentration
        'year': 2021
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)