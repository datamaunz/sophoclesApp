from src.helperFunctions import *
from src.datafile_selection import load_play_text_df

from src.global_page import create_sidebar_1, create_sidebar_2, create_nav_menu_horizontal, generate_global_dfs
from src.visualisations import *
from src.written_summaries import *
from src.initialize_session_state_dict import initialize_session_dict

from src.pages.page_1 import display_page_1
from src.pages.page_2 import display_page_2
from src.pages.page_3 import display_page_3
from src.pages.page_4 import display_page_4


def main():
    
    primaryColor="#ef3340"
     
    st.set_page_config(
        layout="wide",
        page_title="Sophocles App",
        page_icon = "🏹"
        )

    initialize_session_dict()
    st.markdown(
        "## Tiresias: Explore Sophocles' Use of Words"
    )
    st.info("Use the sidebar to select the play and lemmas of interest.")
    
    
    create_sidebar_1()
    create_sidebar_2()
    generate_global_dfs() # st.session_state["all_lemmata_count_dfs"] st.session_state["play_lemmata_df"] st.session_state["unique_lemmata_in_oeuvre"]
    
    
    
    
    
    
    with st.sidebar:
        st.session_state["selected_lemmas"] = st.multiselect(f"Select lemmata from plays of {st.session_state['author']}", st.session_state["unique_lemmata_in_oeuvre"], default=None)
    
    page_names_to_funcs = {
        f"Overview of Play": display_page_1,
        "Selected Lemma Comparison": display_page_2,
        "Significant Differences": display_page_3,
        "Methodology": display_page_4}
    
    
    st.session_state["page_types"] = list(page_names_to_funcs.keys())
    #st.session_state["page_type"] = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
    st.session_state["page_type"] = st.radio("", st.session_state["page_types"], horizontal = True)
    st.divider()
    page_names_to_funcs[st.session_state["page_type"]]()
    
    
    ### Page 1
    #if st.session_state["page_type"] == st.session_state["page_types"][0]:
        
    #    display_page_1()
    
    ### Page 2
    #if st.session_state["page_type"] == st.session_state["page_types"][1]:
        
    #    display_page_2()
    
    ### Page 3  
    #if st.session_state["page_type"] == st.session_state["page_types"][2]:
    #    display_page_3()
        
    ### Page 4
    #if st.session_state["page_type"] == st.session_state["page_types"][3]:
    #    display_page_4()
    
if __name__ == '__main__':
    main()
    