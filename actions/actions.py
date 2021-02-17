# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLive(Action):
    
    def name(self) -> Text:
        return "action_live"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hi, how can I help you?")
        
        return []
 
class ActionResourcesLink(Action):
    
    def name(self) -> Text:
        return "action_resources_link"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="http://www.eap-india.com/resources/")
        
        return []
         
class ActionBook(Action):
    
    def name(self) -> Text:
        return "action_book"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        address = "SP-TBI, Andheri West, Mumbai" 
        
        dispatcher.utter_message(text="Here is the address for your appointment: {}".format(address))
        
        return []
   
class ActionBookTele(Action):
    
    def name(self) -> Text:
        return "action_book_tele"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Your telephonic session has been booked")
        
        return []
         

