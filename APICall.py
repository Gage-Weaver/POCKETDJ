from transformers import pipeline
import requests

pipe = pipeline("image-classification", model="trpakov/vit-face-expression")
def localQuery(filename): #Define Function for Local Queries
    return pipe(filename) #return the value for local model query

def onlineQuery(filename): #Define backup function for online queries
    Api_Token = "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" #Define Api Token Key
    API_URL = "https://api-inference.huggingface.co/models/trpakov/vit-face-expression" #Define url for Api Search
    headers = {"Authorization": f"Bearer {Api_Token}"}
    data = filename
    response = requests.post(API_URL, headers=headers, data=data) #Make an api call
    return response.json()  #Return the result
