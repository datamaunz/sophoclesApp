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


    st.markdown(
        "## Explore Sophocles' Use of Words"
    )
    st.info("Use the sidebar to select the play and lemmas of interest.")
    
    
    
    
    author, play_names, play = create_sidebar() # adopted
    
    page_types = [f"Overview of {play}", "Selected Lemma Comparison", "Significant Differences", "Methodology"]
    page_type = st.radio("", page_types, horizontal = True)
    st.markdown("""---""")
    
        
    all_lemmata_count_dfs = get_lemmata_dfs_stacked(author, play_names)
    
    
    
    
    play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title == play]
    non_play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title != play]
    
    unique_lemmata_in_oeuvre = all_lemmata_count_dfs.lemma.unique()
    
    with st.sidebar:
        selected_lemmas = st.multiselect(f"Select lemmata from plays of {author}", unique_lemmata_in_oeuvre, default=None)
    
    play_lemmata_stats, non_play_lemmata_stats = comparison_of_play_to_others_for_selection(play_lemmata_df, non_play_lemmata_df, selected_lemmas, play_names, play)
    text_df = load_play_text_df(author, selected_lemmas, play)
    
    selected_lemmata_text_df = text_df[text_df.selected_lemmata.isna() == False]
    remaining_selected_lemmata_text_df = text_df[text_df.selected_lemmata.isna() == True]
    
    
    lemma_overview = lemma_stats_across_plays(all_lemmata_count_dfs, selected_lemmas)
    
    if page_type == page_types[0]:
        
        speaker_to_verse_mapping_visual(selected_lemmata_text_df, remaining_selected_lemmata_text_df, play)
        
        if len(selected_lemmata_text_df) > 0:
            st.markdown("---")
            show_verses_with_lemmata(selected_lemmata_text_df)
    
    
    if page_type == page_types[1]:
    
        
        bar_chart_comparison_of_selected_lemmas_all_plays(lemma_overview)
        

    if page_type == page_types[2]:
        
        play_counts_for_comparison_df = compute_counts_for_lemmas_in_plays(all_lemmata_count_dfs, play)
        comp_df = lemma_comparison_with_remaining_plays(play_counts_for_comparison_df, play)
        significant_lemmas = identify_lemmas_with_higher_frequency_than_any_other_play(comp_df)
        significant_lemma_overview = lemma_stats_across_plays(all_lemmata_count_dfs, significant_lemmas)
        bar_chart_comparison_of_selected_lemmas_all_plays(significant_lemma_overview)
        
    if page_type == page_types[3]:
        
        st.markdown(
            "### Data"
        )
        st.markdown(
            "The texts have been obtained from [Perseus](link)."
        )
        
        st.markdown(
            "### Lemmatization"
        )
        st.markdown(
            """None of the existing lemmatizers delivered satisfactory results.
            To make sure this analysis is based on the best available information,
            we scraped the highest ranked lemma for every word directly from Perseus.
            We believe that lemmatizers should work as sequence to sequence models,
            which is why we started building one (see [here](link))."""
        )
        
        st.markdown(
            "### Confidence Intervals"
        )
        st.markdown(
            """
            To determine the significance in differences between 
            """

        )
        
        st.markdown(
            "### Contributors"
        )
        st.markdown(
            "### Funding"
        )
    
if __name__ == '__main__':
    main()
    