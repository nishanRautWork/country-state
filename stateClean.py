import json
input_file_path = './states.json' 
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

transformed_data = []

for state in data:
    slug = f"{state['country_id']}-{state['name'].replace(' ', '').lower()}"
    transformed_state = {
        "id": state["id"],
        "name": state["name"],
        "slug" : slug,
        "countryId":state["country_id"],
        "countryCode":state["country_code"],
        "countryName":state["country_name"]
    }
    transformed_data.append(transformed_state)

output_file_path = 'cleanedStates.json'  
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(transformed_data, output_file, indent=4, ensure_ascii=False) 

print(f"Cleaned data has been saved to {output_file_path}")
