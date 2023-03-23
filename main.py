from Intent import LuisIntent 

app_id = '120aa983-ae16-4a7d-846c-f509628fb4b1'
subscription_key ='30534794ef1143c5917e76fe1d6d42bd' 
endpoint = 'https://predictionintent.cognitiveservices.azure.com' 
recognizer = LuisIntent(app_id, subscription_key, endpoint)

utterance = 'Escape the crowds and soak up the laid-back vibes of Taza'

prediction_json,predection_score,town_name= recognizer.predict(utterance)

print('Intent: {}'.format(prediction_json))
print("-----------------------------------")
print('predection score: {}'.format(predection_score))
print("------------------------------------")
print('the  town name : {}'.format(town_name))
