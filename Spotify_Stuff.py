###Initialize Spotify File
from requests import post, get
import json
import base64
import random
user_id='{user_id}'
user_secret='{user_secret}'
Angry_playlist='0KPEhXA3O9jHFtpd1Ix5OB'
Disgust_playlist='4y61zEEdKhJMaKAGO503Wx'
Fear_playlist='https://api.spotify.com/v1/playlists/{identifier}/tracks'
Happy_playlist='0RH319xCjeU8VyTSqCF6M4'
Sad_playlist='5DVUEqRL1EV8I9n65eBaAw'
Surprise_playlist='https://api.spotify.com/v1/playlists/{identifier}/tracks'
Neutral_playlist='3orcllxQnhCM4lGjrg0Blq'
test_playlist='2z19deYMVB37E938nXNyfv'
def get_token(): #Define a function to get the token 
    auth_str=user_id+':'+user_secret #Concatenate the id and the secret to make one auth string
    auth_byte=auth_str.encode("utf-8") #Encode this string using utf8
    auth_b64=str(base64.b64encode(auth_byte), "utf-8") #Make it base64
    url="https://accounts.spotify.com/api/token" #Define the url to pass token to
    headers= { #Define headers
        "Authorization": "Basic " + auth_b64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data= {"grant_type": "client_credentials"} #Define data that is needed
    result=post(url,headers=headers, data=data) #Define result using post with the url,headers, and data
    json_res=json.loads(result.content) #Json result from result
    token=json_res["access_token"] #Grab token from json results
    return token #Return the token
def get_auth_header(token): #Define function to save work when generating the auth header
    return {"authorization": "Bearer " + token}
def find_songs_by_playlist(token,playlist_id): #Define function to find top 10 songs by artist
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks" #Define url as f string to search with
    headers=get_auth_header(token) #Define headers using earlier function
    result=get(url, headers=headers) #Get result
    json_result=json.loads(result.content) #Grab json data
    return json_result #return the result
token=get_token()
print(find_songs_by_playlist(token,test_playlist))