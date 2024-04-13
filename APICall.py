from transformers import pipeline
import requests

pipe = pipeline("image-classification", model="trpakov/vit-face-expression")
def localQuery(filename):
    return pipe(filename)

def onlineQuery(filename):
    Api_Token = "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"
    API_URL = "https://api-inference.huggingface.co/models/trpakov/vit-face-expression"
    headers = {"Authorization": f"Bearer {Api_Token}"}
    data = filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()