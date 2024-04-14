import streamlit as st
from APICall import * ###Import Query
from streamlit.components.v1 import html
from PlaySpotifySong import addSong
from Spotify_Stuff import search_by_mood
from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
from flask_cors import CORS
import cryptography


app = Flask(__name__)
CORS(app, resources={r"/process-image": {"origins": "https://localhost:5241"}})

def expressAddSong(trackID):
    songEmbed = f"""
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{trackID}?utm_source=generator" width="100%" height="176" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    return songEmbed


@app.route('/process-image', methods=['POST'])
def process_image():
    print(f"Called process_image {request}")
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    image_file = request.files['image']
    image = Image.open(image_file)
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
    st.write(f"We Think that this image is a bit {label}")
    relaventSong = search_by_mood(label)
    relevant_song = expressAddSong(relaventSong)

    print(relaventSong)
    return jsonify({
        'emotion': label,
        'song': relaventSong
    })

if __name__ == '__main__':
    app.run(ssl_context=('publickey.cer', 'privatekey.pem'))






