import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Loaded JSON:", data)

json_string = json.dumps(data, indent=4)
print("JSON string:", json_string)

new_data = {
    "name": "Madi",
    "age": 18,
    "city": "Almaty"
}

with open("output.json", "w") as file:
    json.dump(new_data, file, indent=4)

print("New JSON saved to output.json")
