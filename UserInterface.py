###User Interface
import streamlit as st ###Importing Streamlit 
from AIStuff import query ###Import Query
from ImageProcessing import process_image


camera_input= st.camera_input("Users Webcam", key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False, label_visibility="visible")
file_upload = st.file_uploader("Upload your Picture", type='jpg', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if file_upload is not None:
    process_image(file_upload)

if camera_input is not None:
    process_image(file_upload)


