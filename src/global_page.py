from src.helperFunctions import *
from src.datafile_selection import *

def create_sidebar_1():
    with st.sidebar:
        st.session_state["author"] = st.selectbox("Author", ["Sophocles"], index=0)
        st.session_state["play_names"] = retrieve_play_names(st.session_state["author"])
        
def create_sidebar_2():
    with st.sidebar:
        if st.session_state["play"] == None:
            st.session_state["play"] = st.selectbox("Play", st.session_state["play_names"], index=0)
        else:
            st.session_state["play"] = st.selectbox("Play", st.session_state["play_names"])

def create_nav_menu_horizontal():
    st.session_state["page_types"] = [f"Overview of {st.session_state['play']}", "Selected Lemma Comparison", "Significant Differences", "Methodology"]
    st.session_state["page_type"] = st.radio("", st.session_state["page_types"], horizontal = True)
    st.markdown("""---""")
    
def generate_global_dfs():
    # get global data
    st.session_state["all_lemmata_count_dfs"] = get_lemmata_dfs_stacked(st.session_state["author"], st.session_state["play_names"])
    st.session_state["play_lemmata_df"], st.session_state["non_play_lemmata_df"] = get_play_lemmata_versus_non_play_lemmata(st.session_state["all_lemmata_count_dfs"], st.session_state["play"])
    st.session_state["unique_lemmata_in_oeuvre"] = st.session_state["all_lemmata_count_dfs"].lemma.unique()
    

    
    
    