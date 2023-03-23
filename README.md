# back-endTest_Luis

![image](https://user-images.githubusercontent.com/73289762/227176128-8fe0b00f-e600-4608-a413-e2d6ce79b91f.png)

As we can see in the below screen shot ,the result of retrieving the utterence "Escape the crowds and soak up the laid-back vibes of Taza".
after reciving the response in JSON format we can observe that my intent is 'getTown' and my Luis Model predict that 'Taza' is the town with score=0.98 .

Code Detail :

My class to retrieve intent from the Machine Learning LUIS engine named "LuisIntent".
To create a LuisIntent object we need 3 following  parameters :

#### app id : string 
#### subscription key :string
#### endpoint : string


predict(self, utterance) ,the LuisIntent method take the utternece : string as parameter .

predict() return 
#### data : json format , score :float , town Name :sring

for predicting we need to get the request using the get() <requests> library function, moreover 
this last function need  this params :

           - url= your endpoint+'/luis/prediction/v3.0/apps/'+your  app id+'/slots/staging/predict/'

           - headers = {
                        'Ocp-Apim-Subscription-Key': subscription key
                    }

           - params = {
                        'verbose':{bolean},
                        'log':{bolean},
                        'show-all-intents':{bolean},
                        'query': {string}
                    } 


the response of the get request have a json format,so then we can any Intent value 
