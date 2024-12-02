import json

input_file_path = './states.json'  
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

transformed_data = []
slugs_seen = set() 
for state in data:
    slug = f"{state['country_code'].lower()}-{state['name'].replace(' ', '').lower()}"
    
    if slug not in slugs_seen:
        slugs_seen.add(slug)
        transformed_state = {
            "name": state["name"],
            "slug": slug,
            "countryCode": state["country_code"],
            "countryName": state["country_name"]
        }
        transformed_data.append(transformed_state)

output_file_path = 'cleanedStates.json'  
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(transformed_data, output_file, indent=4, ensure_ascii=False)  

print(f"Cleaned data has been saved to {output_file_path}")
