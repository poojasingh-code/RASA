# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionHelloWorld(Action):
    def name(self) -> Text:
            return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print("this print is from actions.py")   
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionSearchRestaurant(Action):
    def name(self) -> Text:
        return "action_search_restaurant"


    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        
        for e in entities:
            if e['entity'] == 'hotel':
                name = e['value']

            if name == "indian":
                message = "Indian Cuisine Restaurant1, Indian Cuisine Restaurant2, Indian Cuisine Restaurant3, Indian Cuisine Restaurant4"
            if name == "chinese":
                message = "Chinese Cafe 1, Chinese Cafe 2, Chinese Cafe 3, Chinese Cafe 4"
           
        dispatcher.utter_message(text = message)

        return []

class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://api.covid19india.org/data.json").json()
        entities = tracker.latest_message['entities']
        print("last message is", entities)
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        message = "please enter valid state of India!" 

        if state == "india":
            state ="Total"

        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Active : " +data["active"] + " Confirmed : " +data["confirmed"] +" Recovered: " +data["recovered"] + " Last updated on: " +data["lastupdatedtime"]
        dispatcher.utter_message(text = message)

        return []




