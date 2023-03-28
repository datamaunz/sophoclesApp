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
        "## Tiresias: Explore Sophocles' Use of Words"
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
        
        st.info("""
                Only lemmas are shown for which the lower bound of the confidence interval of its frequency
                is larger than the frequency in all other plays.
                """)
        play_counts_for_comparison_df = compute_counts_for_lemmas_in_plays(all_lemmata_count_dfs, play)
        comp_df = lemma_comparison_with_remaining_plays(play_counts_for_comparison_df, play)
        significant_lemmas = identify_lemmas_with_higher_frequency_than_any_other_play(comp_df)
        significant_lemma_overview = lemma_stats_across_plays(all_lemmata_count_dfs, significant_lemmas)
        bar_chart_comparison_of_selected_lemmas_all_plays(significant_lemma_overview)
        
    if page_type == page_types[3]:
        
        
        st.markdown(
            """
            The Github repository of the project can be found [here](https://github.com/datamaunz/sophoclesApp).
            """
        )
        
        st.markdown(
            "### Data"
        )
        st.markdown(
            "The texts have been obtained from [Perseus](http://www.perseus.tufts.edu/hopper/)."
        )
        
        st.markdown(
            "### Lemmatization"
        )
        
        st.info("""
                A *lemma* is the dictionary/citation form of a set of word forms.
                """)
        
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
        
        st.info("""
                By bootstrapping confidence intervals for lemma frequencies in Sophocles' plays, we aim to simulate the lemma frequencies
                that can be expected to be normal given the style of each individual play. These confidence intervals can be used to identify
                statistically signficant differences between lemma frequencies across plays
                (as opposed to differences that could be the result of mere chance).
                """)
        
        st.markdown(
            """
            [Bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) confidence intervals is a statistical technique that involves
            generating many simulated datasets by randomly selecting samples with replacement from the original dataset (in this case, 1000 samples per play).
            By repeatedly calculating a statistic of interest (in this case, word frequencies) for each simulated dataset, 
            we can estimate the distribution of the statistic and use it to calculate the confidence interval.

            The [confidence interval](https://en.wikipedia.org/wiki/Confidence_interval) is a range of values that we can be reasonably
            sure contains the true value of the statistic in the population.
            The bootstrapped confidence interval is often more accurate than traditional methods
            because it accounts for the variability in the data and does not rely on assumptions about the population distribution.
            
            Note the assumption underlying our approach: In contrast to standard use cases of bootstrapping,
            we do know the true frequency of all words in all plays.
            The bootstrapped confidence intervals are used to simulate the distribution
            of word frequencies that can be expected for any play written in this particular style.
            """

        )
        
        st.markdown(
            "### Contributors"
        )
        
        st.markdown(
            """
            - [**Ben Folit-Weinberg**](https://research-information.bris.ac.uk/en/persons/benjamin-folit-weinberg): idea, conception and oversight
            - [**Justus Schollmeyer**](https://www.linkedin.com/in/justus-schollmeyer-014a2314b/): creation of the app and methodology
            - [**Tom Odhiambo**](https://www.linkedin.com/in/tom-odhiambo/): work on sequence to sequence model for improved lemmatization"""
        )
        
        st.markdown(
            "### Acknowledgement"
        )
        st.markdown(
            "We are grateful for the funding of the project by:"
        )
        
        
        col1, col2, col3 = st.columns(3)
        col1.image('dataFiles/images/Sophocles_funders.001.jpeg', caption="The Jean Golding Institute", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        col2.image('dataFiles/images/Sophocles_funders.002.jpeg', caption="The A.G. Leventis Foundation", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        col3.image('dataFiles/images/Sophocles_funders.003.jpeg', caption="The British Academy", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        
    
if __name__ == '__main__':
    main()
    