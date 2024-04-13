import requests


Api_Token = "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"
API_URL = "https://api-inference.huggingface.co/models/trpakov/vit-face-expression"
headers = {"Authorization": f"Bearer {Api_Token}"}

def query(filename):
    data = filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


