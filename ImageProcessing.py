import streamlit as st
from APICall import * ###Import Query
from streamlit.components.v1 import html
from PlaySpotifySong import addSong
from Spotify_Stuff import search_by_mood


def process_image(image):


    emotion_list = []
    try:
        result = localQuery(image)
    except:
        result= onlineQuery(image)
    #Result is a list of dictionaries, ranging from 0 Most Likely to 6 Least Likely

    for emotion in result:
        #Add Each Dictionary to our local list
        emotion_list.append(emotion)


    most_likely_emotion = emotion_list[0]
    label = most_likely_emotion["label"]

    # Execute your app
    st.write(f"We Think that this image is a bit {label}, Here is what we recommend")
    relaventSong = search_by_mood(label)
    addSong(relaventSong)





