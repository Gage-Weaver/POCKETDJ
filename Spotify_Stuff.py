###Initialize Spotify File
from requests import post, get
import json
import base64
import random
user_id='799c19d6aa3340ccb09415c0fe2a5741'
user_secret='2164e6a8233649b483306e1726ab3038'
Angry_artists=["Gum Bleed"]
Disgust_artists=["Zach Bryan"]
Fear_artists=["Tyler, The Creator"]
Happy_artists=["Pharell Williams"]
Sad_artists=["Joji"]
Surprise_artists=["Mozart"]
Neutral_artists=["Taylor Swift"]
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
def search_for_artist(token, artist): #Define function to search for an artist by name and get their id which is needed to get songs
    url= "https://api.spotify.com/v1/search" #Define url for this search
    headers=get_auth_header(token) #Use the earlier function that generates header and assign to headers
    query=f"?q={artist}&type=artist&limit=1" #Assign query with limit 1 to only grab first artist that comes up
    query_url=url+query #Combine url and query 
    result=get(query_url, headers=headers) #Get the result using headers and query url
    json_result=json.loads(result.content)["artists"]["items"] #Grab the result in json form
    if len(json_result) == 0: #if no result return none
        return None
    return json_result[0] #If there is a result return it
def find_songs_by_artist(token,artist_id): #Define function to find top 10 songs by artist
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US" #Define url as f string to search with
    headers=get_auth_header(token) #Define headers using earlier function
    result=get(url, headers=headers) #Get result
    json_result=json.loads(result.content)["tracks"] #Grab json data
    return json_result #return the result
token=get_token()
def search_by_artist_name(token,artist):
    artist_identifier=search_for_artist(token,artist)
    artist_id=artist_identifier["id"] #Define artist_id using result function
    songs= find_songs_by_artist(token,artist_id) #Define songs using the find songs function
    songslist=[]
    for song in songs: #Loop through songs and print them out nicely
        songslist.append(song['id'])
    return(random.choice(songslist))
def search_by_mood(token,mood):
    if mood=="angry":
        artist=random.choice(Angry_artists)
    elif mood=="disgust":
        artist=random.choice(Disgust_artists)
    elif mood=="fear":
        artist=random.choice(Fear_artists)
    elif mood=="happy":
        artist=random.choice(Happy_artists)
    elif mood=="sad":
        artist=random.choice(Sad_artists)
    elif mood=="surprise":
        artist=random.choice(Surprise_artists)
    elif mood=="disgust":
        artist=random.choice(Neutral_artists)
    return(search_by_artist_name(token,artist))




