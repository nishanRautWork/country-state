import json

country_path = 'cleanedCountries.json'
with open(country_path, 'r', encoding='utf-8') as file:
    cleaned_data = json.load(file)

country_names = set()
duplicates_countries = []

for country in cleaned_data:
    slug = country['slug']
    if slug in country_names:
        duplicates_countries.append(slug)  
    else:
        country_names.add(slug)  

if duplicates_countries:
    print("Duplicate country names found:")
    for duplicate in set(duplicates_countries):  
        print(duplicate)
else:
    print("No duplicate country names found.")


state_path='cleanedStates.json'
with open(state_path, 'r', encoding='utf-8') as file:
    cleaned_data_state = json.load(file)

state_names = set()
duplicates_state = []

for state in cleaned_data_state:
    slug = state['slug']
    if slug in state_names:
        duplicates_state.append(slug)
    else:
        state_names.add(slug)  


if duplicates_state:
    print("Duplicate state names found:")
    for duplicate in set(duplicates_state):  
        print(duplicate)
    
else:
    print("No duplicate state names found.")


print("This is country names count: ",len(country_names))
print("This is state name count",len(state_names))




