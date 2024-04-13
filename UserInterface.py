###User Interface
import streamlit as st ###Importing Streamlit 
from APICall import * ###Import Query
from ImageProcessing import process_image

from tempfile import NamedTemporaryFile

camera_input= st.camera_input("Users Webcam", key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False, label_visibility="visible")
file_upload = st.file_uploader("Upload your Picture", type='jpg', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if file_upload is not None:
    f = file_upload

    with NamedTemporaryFile(dir='.', suffix='.csv') as f:
        f.write(file_upload.getbuffer())
        process_image(f.name)

if camera_input is not None:
    f = camera_input

    with NamedTemporaryFile(dir='.', suffix='.csv') as f:
        f.write(camera_input.getbuffer())
        process_image(f.name)

