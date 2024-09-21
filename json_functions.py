import json

# Get API Key : <https://openweathermap.org/api>
def read_json(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)

# Write API request result into json file
def write_json(path, json_data):
    with open(path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)