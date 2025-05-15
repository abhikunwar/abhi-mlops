from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from config import *
import os
from utils.common_functions import read_yml

config_yaml_file = read_yml('path_config.yaml')
model_path = os.path.join(config_yaml_file['model_saving_path']['model_dir_path'],config_yaml_file['model_saving_path']['model_file_name'])


app = Flask(__name__)

# Load the trained model

MODEL_PATH = model_path

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print("⚠️ Model file not found. Please check the path.")

# Define the required input features
FEATURES = [
    'no_of_adults', 'no_of_children', 'no_of_weekend_nights',
    'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space',
    'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month',
    'arrival_date', 'market_segment_type', 'repeated_guest',
    'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
    'avg_price_per_room', 'no_of_special_requests'
]

# Simple encoders (for demo purposes)
meal_plan_map = {
    "Not Selected": 0,
    "Meal Plan 1": 1,
    "Meal Plan 2": 2,
    "Meal Plan 3": 3
}
room_type_map = {
    "Room_Type 1": 1,
    "Room_Type 2": 2,
    "Room_Type 3": 3,
    "Room_Type 4": 4
}
market_segment_map = {
    "Online": 1,
    "Offline": 2,
    "Corporate": 3,
    "Aviation": 4
}

def encode_input(data):
    """Encode categorical variables manually."""
    return [
        data['no_of_adults'],
        data['no_of_children'],
        data['no_of_weekend_nights'],
        data['no_of_week_nights'],
        meal_plan_map.get(data['type_of_meal_plan'], 0),
        data['required_car_parking_space'],
        room_type_map.get(data['room_type_reserved'], 1),
        data['lead_time'],
        data['arrival_year'],
        data['arrival_month'],
        data['arrival_date'],
        market_segment_map.get(data['market_segment_type'], 1),
        data['repeated_guest'],
        data['no_of_previous_cancellations'],
        data['no_of_previous_bookings_not_canceled'],
        data['avg_price_per_room'],
        data['no_of_special_requests']
    ]

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded. Check model path.'}), 500

    data = request.get_json()

    # Check for missing fields
    missing = [field for field in FEATURES if field not in data]
    if missing:
        return jsonify({'error': f'Missing fields: {missing}'}), 400

    try:
        input_vector = np.array([encode_input(data)])
        prediction = model.predict(input_vector)[0]

        return jsonify({
            'input': data,
            'prediction': int(prediction)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
