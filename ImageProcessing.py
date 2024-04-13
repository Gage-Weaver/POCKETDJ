import streamlit as st
from AIStuff import query ###Import Query


def process_image(image):
    emotion_list = []
    result = query(image)
    #Result is a list of dictionaries, ranging from 0 Most Likely to 6 Least Likely


    for emotion in result:
        #Add Each Dictionary to our local list
        emotion_list.append(emotion)


    most_likely_emotion = emotion_list[0]
    label = most_likely_emotion['label']

    st.write(label)

