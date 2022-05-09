from src.helperFunctions import *
from src.datafile_selection import *
from src.lemmata_comparison import *
from src.sidebar import *
from src.visualisations import *
from src.written_summaries import *
import os


def main():
    
    primaryColor="#ef3340"
     
    st.set_page_config(
        layout="wide",
        page_title="Sophocles App",
        page_icon = "🏹"
        )

    
    
    author, play_names, play = create_sidebar()
    
    st.markdown(f"## {play}")
        
    all_lemmata_count_dfs = get_lemmata_dfs_stacked(author, play_names)
    
    
    play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title == play]
    non_play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title != play]
    
    unique_lemmata_in_oeuvre = all_lemmata_count_dfs.lemma.unique()
    
    selected_lemmata = st.multiselect(f"Select lemmata from plays of {author}", unique_lemmata_in_oeuvre, default=None)
    
    play_lemmata_stats, non_play_lemmata_stats = comparison_of_play_to_others_for_selection(play_lemmata_df, non_play_lemmata_df, selected_lemmata, play_names, play)
    text_df = load_play_text_df(author, selected_lemmata, play)
    
    selected_lemmata_text_df = text_df[text_df.selected_lemmata.isna() == False]
    remaining_selected_lemmata_text_df = text_df[text_df.selected_lemmata.isna() == True]
    
    """---"""    
    
    write_comparison_in_words(non_play_lemmata_stats, selected_lemmata, play)

    """---"""
    show_verses_with_lemmata(selected_lemmata_text_df)
    
    """---"""
    
    speaker_to_verse_mapping_visual(selected_lemmata_text_df, remaining_selected_lemmata_text_df, play)
    
if __name__ == '__main__':
    main()
    