from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateNameForm(FormValidationAction):
# class ValidateNameForm(Action):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_a_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `a_first_name` value."""
        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}

    # def validate_last_name(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `last_name` value."""
    #     # If the name is super short, it might be wrong.
    #     print(f"Last name given = {slot_value} length = {len(slot_value)}")
    #     if len(slot_value) <= 2:
    #         dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
    #         return {"last_name": None}
    #     else:
    #         return {"last_name": slot_value}
    #
    #
    # def validate_genero(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `genero` value."""
    #     # If the name is super short, it might be wrong.
    #     print(f"Género leído = {slot_value} length = {len(slot_value)}")
    #     if {slot_value} != "hombre" or {slot_value} != "mujer":
    #         dispatcher.utter_message(text=f"No entiendo tu respuesta. Recuerda digitar si eres hombre o mujer.")
    #         return {"genero": None}
    #     else:
    #         return {"genero": slot_value}
    #
    #
    # def validate_fumador(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `fumador` value."""
    #     # If the name is super short, it might be wrong.
    #     print(f"Fumador leído = {slot_value} length = {len(slot_value)}")
    #     if len(slot_value) <= 1:
    #         dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
    #         return {"fumador": None}
    #     else:
    #         return {"fumador": slot_value}
    #
    #
    # def validate_peso(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `peso` value."""
    #     # If the name is super short, it might be wrong.
    #     print(f"Peso leído = {slot_value} length = {len(slot_value)}")
    #     if len(slot_value) <= 1:
    #         dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
    #         return {"peso": None}
    #     else:
    #         return {"peso": slot_value}
