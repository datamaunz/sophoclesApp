from src.helperFunctions import *
from src.datafile_selection import *

def create_sidebar():
    with st.sidebar:
        author = st.selectbox("Author", ["Sophocles"], index=0)
        play_names = retrieve_play_names(author)
        play = st.selectbox("Play", play_names, index=0)
    return author, play_names, play