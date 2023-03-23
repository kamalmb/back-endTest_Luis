import requests
import json

class LuisIntent:
    def __init__(self, app_id, subscription_key, endpoint):
        self.subscription_key = subscription_key
        self.endpoint = endpoint
        self.app_id = app_id

    def predict(self, utterance):
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        params = {
            'verbose':True,
            'log':False,
            'show-all-intents':True,
            'query': utterance
        }
        url=self.endpoint+'/luis/prediction/v3.0/apps/'+self.app_id+'/slots/staging/predict/'
        try :
            response = requests.get(url, params=params,headers=headers)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            
        data = json.loads(response.content.decode('utf-8-sig'))
        townName = data['prediction']['entities']['TownName']
        score = data['prediction']['intents']['getTowns']['score']
        return data,score,townName


#curl "https://predictionintent.cognitiveservices.azure.com/luis/prediction/v3.0/apps/120aa983-ae16-4a7d-846c-f509628fb4b1/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=30534794ef1143c5917e76fe1d6d42bd&query=YOUR_QUERY_HERE"
