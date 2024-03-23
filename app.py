from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[' http://localhost:3000'])  # Replace with your React app's origin

# Sample endpoint to fetch deforestation data
@app.route('/deforestation-data', methods=['POST'])
def get_deforestation_data():
    # Replace this with actual data retrieval logic
    data = {
        'region': 'Amazon Rainforest',
        'deforestation_rate': 0.05,  # Example deforestation rate
        'year': 2021
    }
    return jsonify(data)

# Sample endpoint to fetch climate change data
@app.route('/climate-change-data', methods=['POST'])
def get_climate_change_data():
    # Replace this with actual data retrieval logic
    data = {
        'region': 'Global',
        'temperature_anomaly': 1.2,  # Example temperature anomaly
        'year': 2021
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
