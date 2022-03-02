from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
import numpy as np
import pickle
import joblib
from tensorflow.keras.models import  load_model
import json

class ValidateNombreForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_nombre_form"   
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:
        return []
    def validate_a_nombre(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
            ) -> Dict[Text, Any]:
            """ Validate Slot Value. """
            if not slot_value:
                return {"a_nombre": None}
            else:
                return {"a_nombre": slot_value}

class ActionLongitudNombre(Action):
    def name(self) -> Text:
        return "action_longitud_nombre"
    def run(
            self,
            dispatcher, 
            tracker: Tracker,
            domain: DomainDict,
            ) -> List[Dict[Text, Any]]:

            nombre = tracker.get_slot('a_nombre')
            if len(nombre) <= 2:
                dispatcher.utter_message(text="El nombre que me dices es muy corto. Revisa si lo digitaste correctamente.")
                #dispatcher.utter_message(buttons = [
                #    {"payload": "/afirmar", "title": "Sí, es mi nombre."},
                #    {"payload": "/nombre_equivocado", "title": "¡¡Upss!! Me equivoqué. ¡Quiero volver a decirte mi nombre!"}, 
                #])

                #dispatcher.utter_message(text='Prueba')
#                if tracker.get_intent_of_latest_message = 'nombre_equivocado':
#                    return {'a_nombre': }
                return[]
                #return {"a_nombre": nombre}
            #else:
            #    return {"a_nombre": nombre}


#Obtener respuestas del usuario
class ActionGetUserVals(FormValidationAction):
    def name(self) -> Text:
        return "action_get_user_vals"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
#            domain: DomainDict,
            domain: Dict[Text, Any],
#            ) -> List[Dict[Text, Any]]:
           ) -> List[EventType]:  
        #Obtener valores de los slots
        nombre = tracker.get_slot('a_nombre')
        edad = int(tracker.get_slot('b_edad'))
        colesterol_hdl = int(tracker.get_slot('c_colesterol_hdl'))
        genero = tracker.get_slot('d_genero')
        colesterol_total = int(tracker.get_slot('e_colesterol_total'))        
        cardiacos = tracker.get_slot('f_antecedentes_cardiacos')
        pa1 = int(tracker.get_slot('g_presion_sistolica'))
        trigliceridos = int(tracker.get_slot('h_trigliceridos'))
        colesterol_ldl = int(tracker.get_slot('i_colesterol_ldl'))
        
        #Transfomación de datos
        if genero == 'hombre':
            genero = 1
        else:
            genero = 0

        if cardiacos == 'Si':
            cardiacos = 1
        else:
            cardiacos = 0

        data = np.array([edad, colesterol_hdl, genero, colesterol_total, cardiacos, pa1, trigliceridos, colesterol_ldl])
        dispatcher.utter_message(text="Estoy procesando la información que me brindaste...")
#        dispatcher.utter_message(text=print(data))
        #loaded_model = joblib.load("./elison_rfc_sub.joblib")
        #pickle.dump(xg_class, open("elison_xgboost_sub.dat", "wb"))
        loaded_model = load_model('elison_rna3.h5',compile=False)
        #loaded_model = pickle.load(open("elison_xgboost_sub_cb.pkl", "rb"))

        #Predecir riesgo cardiovascular
        rcv_pred = loaded_model.predict(data.reshape(1,8))
                
        ##************************************************
        ##Esto aplica solo para modelos basados en Xgboost
        #Convertir indicador número de rcv a textoi
        #rcv = ""
        #if rcv_pred == 0:
        #    rcv = "Bajo"
        #if rcv_pred == 1:
        #    rcv = "Intermedio"
        #if rcv_pred == 2:
        #    rcv = "Alto"
        
        #Mostrar resultado en pantalla
        #dispatcher.utter_message(text="Tu nivel de riesgo cardiovascular es: ")
        #dispatcher.utter_message(text=rcv)
        ##************************************************
        
        class NumpyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                return json.JSONEncoder.default(self, obj)

        #a = np.array([[1, 2, 3], [4, 5, 6]])
        a=np.array(rcv_pred)       
        json_dump = json.dumps({'Bajo': a[0][0]*100, 'Latente': a[0][1]*100, 'Alto': a[0][2]*100}, cls=NumpyEncoder)
        print(json_dump)


        #Mostrar resultado en pantalla
        dispatcher.utter_message(text="Tu probabilidad de riesgo cardiovascular expresada en porcentaje es: ")
        dispatcher.utter_message(json_dump)    
    

        return []


#class ValidateNameForm(Action):
#    def name(self) -> Text:
#        return "validate_name_form"
#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        dispatcher.utter_message(text="Probando custom actions")
#        nombre = tracker.get_slot('a_first_name')
#        if len(nombre) <= 2:
#            dispatcher.utter_message(text="That's a very short name. I'm assuming you mis-spelled.")
#        return[]




        #"""Validate `a_first_name` value."""
        ## If the name is super short, it might be wrong.
        #print(f"First name given = {slot_value} length = {len(slot_value)}")
        #if len(slot_value) <= 2:
        #    dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        #    return {"first_name": None}
        #else:
        #    return {"first_name": slot_value}

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
