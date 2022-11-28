import requests

url = "https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg"

data = {"url": url}

result = requests.post(
    "http://localhost:8080/2015-03-31/functions/function/invocations", json=data
).json()

print(result)
