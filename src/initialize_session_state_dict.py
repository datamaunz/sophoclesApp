import streamlit as st


def initialize_session_dict():
    if "author" not in st.session_state:
        st.session_state["author"] = None
    if "play_names" not in st.session_state:
        st.session_state["play_names"] = None
    if "play" not in st.session_state:
        st.session_state["play"] = None
    if "page_types" not in st.session_state:
        st.session_state["page_types"] = None
    if "page_type" not in st.session_state:
        st.session_state["page_type"] = None
    if "all_lemmata_count_dfs" not in st.session_state:
        st.session_state["all_lemmata_count_dfs"] = None
    if "play_lemmata_df" not in st.session_state:
        st.session_state["play_lemmata_df"] = None
    if "non_play_lemmata_df" not in st.session_state:
        st.session_state["non_play_lemmata_df"] = None
    if "unique_lemmata_in_oeuvre" not in st.session_state:
        st.session_state["unique_lemmata_in_oeuvre"] = None    
    if "selected_lemmas" not in st.session_state:
        st.session_state["selected_lemmas"] = None    
    if "text_df" not in st.session_state:
        st.session_state["text_df"] = None    
    if "selected_lemmata_text_df" not in st.session_state:
        st.session_state["selected_lemmata_text_df"] = None    
    if "remaining_selected_lemmata_text_df" not in st.session_state:
        st.session_state["remaining_selected_lemmata_text_df"] = None        
    if "lemma_overview" not in st.session_state:
        st.session_state["lemma_overview"] = None         