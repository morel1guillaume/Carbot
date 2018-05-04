# Ref: https://github.com/bhavaniravi/rasa-site-bot
from flask import Flask
from flask import render_template,jsonify,request
import requests
# from models import *
from engine import *
import random
from rasa_core.actions import Action
from rasa_core.events import SlotSet


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
        intent = response.get("next_action")
        tracker = response.get("tracker")
        slots = tracker.get("slots")
        sender_id = tracker.get("sender_id")
        is_RH = slots.get("is_RH")
        print(is_RH)
        print(sender_id)
        print('hello')
        print(intent)
        #print("Intent {}, Entities {}".format(intent,entities))
        if intent == "action_pneu":
            print("hello je suis là")
            # payload = {"executed_action": "utter_RH", "events": [{"event": "slot", "name": "is_RH", "value": 1}]}
            # responsetoast = requests.post("http://localhost:5005/conversations/default/continue", json=payload)


            url = "http://localhost:5005/conversations/default/continue"

            payload = "{\n\t\"executed_action\": \"utter_bonjour\",\n\t\"events\": [\n\t\t{\n\t\t\t\"event\": \"slot\", \"name\": \"is_RH\", \"value\": 1\n\t\t\t\n\t\t}\n\t\t]\n}"
            headers = {
                'Content-Type': "application/json",
                'Cache-Control': "no-cache",
                'Postman-Token': "c81b99cf-6df5-41e2-a2d6-f0b397736616"
                }

            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            response_text = "IS RH"# "Sorry will get answer soon" #get_event(entities["day"],entities["time"],entities["place"])
        else:
            response_text = get_random_response(intent)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
    
#{"executed_action": "utter_bonjour","events": [{"event": "slot", "name": "is_RH", "value": TRUE}]}