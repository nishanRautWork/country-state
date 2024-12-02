import json
input_file_path = './countries.json' 
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

transformed_data = []

for country in data:
    slug = f"{country['name'].replace(' ', '').lower()}"
    transformed_country = {
        "name": country["name"],
        "iso3": country["iso3"],
        "iso2": country["iso2"],
        "numericCode": country["numeric_code"],
        "phoneCode": country["phone_code"],
        "currency": country["currency"],
        "currencySymbol": country["currency_symbol"],
        "timeZone": country["timezones"][0]["gmtOffsetName"],  # Taking primary timezone
        "slug": slug  # Adding slug in lowercase
    }
    transformed_data.append(transformed_country)

output_file_path = 'cleanedCountries.json'  
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(transformed_data, output_file, indent=4, ensure_ascii=False) 

print(f"Cleaned data has been saved to {output_file_path}")
