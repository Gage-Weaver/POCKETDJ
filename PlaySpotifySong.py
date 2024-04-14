import streamlit as st ###Importing Streamlit
from streamlit.components.v1 import html

def addSong(trackID):

    songEmbed =f"""
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{trackID}?utm_source=generator" width="100%" height="176" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""

    html(songEmbed)