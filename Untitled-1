import requests

url = "http://localhost:5005/conversations/default/continue"

payload = "{\n\t\"executed_action\": \"utter_bonjour\",\n\t\"events\": [\n\t\t{\n\t\t\t\"event\": \"slot\", \"name\": \"is_RH\", \"value\": 1\n\t\t\t\n\t\t}\n\t\t]\n}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "c81b99cf-6df5-41e2-a2d6-f0b397736616"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)