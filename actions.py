
from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionCustom(Action):
    def name(self):
        return "action_custom"

    def run(self, dispatcher, tracker, domain):
        # send utter default template to user
        dispatcher.utter_template("utter_default")
        # ... other code
        return [SlotSet("is_RH", True)]


class ActionPneu(Action):

    def name(self):
        return "action_pneu"

    def run(self, dispatcher, tracker, domain):
        a = tracker.get_slot('is_RH')
        if a:
            # send utter default template to user
            dispatcher.utter_template("utter_pneu_1")

        else:
            dispatcher.utter_template("utter_pneu_2")

        # ... other code
        return []


if __name__ == '__main__':
    print("hello")
