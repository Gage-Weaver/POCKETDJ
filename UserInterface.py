###User Interface
import streamlit as st ###Importing Streamlit 
from AIStuff import query ###Import Query
camera_input= st.camera_input("Users Webcam", key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False, label_visibility="visible")
file_upload = st.file_uploader("Upload your Picture", type='jpg', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
if file_upload is not None: ###(Need to add support for different file types, specifically heic)
    st.write(query(file_upload))
if camera_input is not None:
    st.write(query(camera_input))

