###User Interface
import streamlit as st ###Importing Streamlit 
from APICall import * ###Import Query
from ImageProcessing import process_image
from Spotify_Stuff import add_to_dict

from tempfile import NamedTemporaryFile

camera_input= st.camera_input("Camera Input", key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False, label_visibility="visible")
file_upload = st.file_uploader("Upload your Picture", type='jpg', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if file_upload is not None:
    f = file_upload
    process_image(f)
    
    #with NamedTemporaryFile(dir='.', suffix='.csv') as f:
        #f.write(file_upload.getbuffer())
        #process_image(f.name)
        

if camera_input is not None:
    f = camera_input
    process_image(f)

    #with NamedTemporaryFile(dir='.', suffix='.csv') as f:
        #f.write(camera_input.getbuffer())
        #process_image(f.name)
st.write("Add an artist?")
with st.form(key='Add_Artist'):
    artist_input= st.text_input("Artist Name")
    mood = st.selectbox("What Mood Category Is This Artist?",['angry','disgust','fear','happy','sad','surprise','neutral'])
    submit = st.form_submit_button("Submit")
if submit:
    add_to_dict(mood,artist_input)
