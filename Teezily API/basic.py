import requests
import json
# parameters = {"lat": 40.71, "lon": -74}

# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.content.decode('utf-8'))

# best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
# best_food_chains_string = json.dumps(best_food_chains)
# print(type(best_food_chains_string)) 
# print(type(json.loads(best_food_chains_string)))

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
data = response.json()
print(type(data))
print(data)
print(response.headers)
print(response.headers["content-type"])