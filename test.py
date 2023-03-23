from Intent import LuisIntent 



def test_prediction_town_name():
    app_id = '120aa983-ae16-4a7d-846c-f509628fb4b1'
    subscription_key ='30534794ef1143c5917e76fe1d6d42bd' 
    endpoint = 'https://predictionintent.cognitiveservices.azure.com' 
    recognizer = LuisIntent(app_id, subscription_key, endpoint)

    utterance = 'Escape the crowds and soak up the laid-back vibes of Taza'

    #here i wanna test in if return me the exact town name

    assert " ".join(str(x) for x in (recognizer.predict(utterance)[2])) == "Taza"