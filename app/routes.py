from flask import Blueprint, request, jsonify
import os
import json

main = Blueprint('main', __name__)

@main.route('/save', methods=['POST'])
def save_json():
    data = request.get_json()
    app_name = data['AppName']
    username = data['Username']
    config_name = data['JsonConfigName']
    json_body = data['JSON']

    # Ensure the directory exists
    directory = f"./storage/{app_name}/{username}"
    os.makedirs(directory, exist_ok=True)

    # Save the JSON file
    file_path = f"{directory}/{config_name}.json"
    with open(file_path, 'w') as json_file:
        json.dump(json_body, json_file)

    return jsonify({"message": "JSON saved successfully"}), 201

