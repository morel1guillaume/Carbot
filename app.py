# Ref: https://github.com/bhavaniravi/rasa-site-bot
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random
from rasa_core.actions import Action
from rasa_core.events import SlotSet
import json


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])



@app.route('/chat',methods=["POST"])
def chat():
    
    try:
        entities=None
        user_message = request.form["text"]
        response = requests.get("http://localhost:5005/conversations/default/parse?", params={"q":user_message})
        response = response.json()
        #entities = response.get("entities")
        #topresponse = response["topScoringIntent"]
        next_action = response.get("next_action")
        tracker = response.get("tracker")
        slots = tracker.get("slots")
        sender_id = tracker.get("sender_id")
        is_RH = slots.get("is_RH")
        print(is_RH)
        print(sender_id)
        print('hello')
        print(next_action)
        #print("Intent {}, Entities {}".format(intent,entities))
        with open('template.json') as f:
            data_json = json.load(f)
        print(data_json)

        if next_action in data_json:
            url = "http://localhost:5005/conversations/default/continue"
            payload = "{\n\t\"executed_action\": " + next_action + ",\n\t\"events\": []\n}"
            print(payload)
            # payload = "{\n\t\"executed_action\": " + next_action + ",\n\t\"events\": [\n\t\t{\n\t\t\t\"event\": \"slot\", \"name\": \"is_RH\", \"value\": 1\n\t\t\t\n\t\t}\n\t\t]\n}"
            headers = {
                'Content-Type': "application/json",
                'Cache-Control': "no-cache",
                'Postman-Token': "c81b99cf-6df5-41e2-a2d6-f0b397736616"
                }

            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            print(data_json[next_action]['text'])
            response_text = data_json[next_action]['text']
        else:
            response_text = get_random_response(next_action)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
    
#{"executed_action": "utter_bonjour","events": [{"event": "slot", "name": "is_RH", "value": TRUE}]}