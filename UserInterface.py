###User Interface
import streamlit as st ###Importing Streamlit 
from AIStuff import query
st.camera_input("Users Webcam", key=None, help=None, on_change=None, args=None, kwargs=None,disabled=False, label_visibility="visible")
file_upload = st.file_uploader("Upload your Picture", type='jpg', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
if file_upload is not None:
    st.write(query(file_upload))

