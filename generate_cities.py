import json

usa_cities = [
"New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Antonio","San Diego","Dallas","San Jose",
"Austin","Jacksonville","Fort Worth","Columbus","Charlotte","San Francisco","Indianapolis","Seattle","Denver","Washington",
"Boston","El Paso","Nashville","Detroit","Oklahoma City","Portland","Las Vegas","Memphis","Louisville","Baltimore",
"Milwaukee","Albuquerque","Tucson","Fresno","Sacramento","Kansas City","Atlanta","Miami","Raleigh","Omaha",
"Minneapolis","Tulsa","Wichita","New Orleans","Arlington","Cleveland","Bakersfield","Tampa","Aurora","Honolulu"
]

canada_cities = [
"Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa","Winnipeg","Quebec City","Hamilton","Kitchener",
"London","Victoria","Halifax","Oshawa","Windsor","Saskatoon","Regina","St. John's","Barrie","Kelowna",
"Abbotsford","Kingston","Sudbury","Sherbrooke","Trois-Rivières","Guelph","Cambridge","Whitby","Ajax","Coquitlam"
]

suffixes = [
"Downtown","North","South","East","West","Central","Metro Area","Suburbs","City Center"
]

cities = []

# Build expanded dataset
for city in usa_cities:
    cities.append(city)
    for s in suffixes:
        cities.append(f"{city} {s}")

for city in canada_cities:
    cities.append(city)
    for s in suffixes:
        cities.append(f"{city} {s}")

# Fill until 5000
i = 0
base_pool = usa_cities + canada_cities

while len(cities) < 5000:
    base = base_pool[i % len(base_pool)]
    cities.append(f"{base} Area {i}")
    i += 1

cities = cities[:5000]

with open("cities.json", "w", encoding="utf-8") as f:
    json.dump(cities, f, indent=2)

print("Generated cities:", len(cities))
