import streamlit as st
import pandas as pd
import numpy as np

from src.lemmata_comparison import compute_counts_for_lemmas_in_plays, lemma_stats_across_plays
from src.pages.page_2 import bar_chart_comparison_of_selected_lemmas_all_plays



@st.cache_data
def identify_lemmas_with_higher_frequency_than_any_other_play(comp_df, n_remaining_plays, n_more_frequent):
    
    comp_score = n_more_frequent / n_remaining_plays
    significant_comp = comp_df[comp_df.comparison >= comp_score]
    significant_lemmas = significant_comp.index.to_list()
    return significant_lemmas

@st.cache_data
def identify_lemmas_with_lower_frequency_than_any_other_play(comp_df, n_remaining_plays, n_less_frequent):
    
    comp_score = n_less_frequent / n_remaining_plays
    significant_comp = comp_df[comp_df.comparison >= comp_score]
    significant_lemmas = significant_comp.index.to_list()
    return significant_lemmas

@st.cache_data
def identify_lemmas_with_higher_frequency_than_at_least_one_other_play(comp_df):
    significant_comp = comp_df[comp_df.comparison > 0]
    kind_of_significant_lemmas = significant_comp.index.to_list()
    return kind_of_significant_lemmas

@st.cache_data
def lemma_comparison_with_remaining_plays(play_counts_for_comparison_df, play, higher):
    
    if higher == True:
        play_counts_for_comparison_df["comparison"] = play_counts_for_comparison_df[f"LOW_perc_{play}"] > play_counts_for_comparison_df[f"COUNT_perc"]
    else:
        play_counts_for_comparison_df["comparison"] = play_counts_for_comparison_df[f"HIGH_perc_{play}"] < play_counts_for_comparison_df[f"COUNT_perc"]
    num_cols = list(play_counts_for_comparison_df.select_dtypes(include=np.number).columns)
    comp_df = play_counts_for_comparison_df[num_cols + ["lemma", "comparison"]].groupby("lemma").mean()
    return comp_df

@st.cache_data
def create_pivot_table(significant_lemma_overview):
        pivot_df = significant_lemma_overview[["lemma", "COUNT", "play_name"]].pivot(index='lemma', columns='play_name', values='COUNT')
        pivot_df = pivot_df[[st.session_state["play"]] + [x for x in pivot_df.columns if x not in [st.session_state["play"]]]].sort_values(st.session_state["play"], ascending=False).fillna(0)
        return pivot_df

def display_page_3():

    
    
    
    play_counts_for_comparison_df = compute_counts_for_lemmas_in_plays(st.session_state["all_lemmata_count_dfs"], st.session_state["play"])
    
    n_remaining_plays =  len(play_counts_for_comparison_df["play_name"].unique())
    play_comp_choices = [x for x in range(1,n_remaining_plays+1)][::-1]
    
    #col1, col2= st.columns(2)
    col1, col2, col3= st.columns([0.5, 0.25, 0.25])
    
    comp_type = col2.radio("More frequent or less frequent?", ["more frequent", "less frequent"], horizontal=True)
    
    
    #n_more_frequent = col2.selectbox("More frequent than in at least X other plays", play_comp_choices, index=0)
    
    if comp_type == "more frequent":
    
        n_comp_frequent = col3.number_input(label = "More frequent than in at least X other plays", min_value=1, max_value=n_remaining_plays, value=6)
        col1.info(f"""Only lemmas are shown for which the lower bound of the confidence interval of its frequency
                is larger than the frequency in at least {n_comp_frequent} other plays (compared to the {n_remaining_plays} other plays by {st.session_state['author']}).
                """)
        higher=True
    
    else:
        
        n_comp_frequent = col3.number_input(label = "Less frequent than in at least X other plays", min_value=1, max_value=n_remaining_plays, value=6)
        col1.info(f"""Only lemmas are shown for which the upper bound of the confidence interval of its frequency
                is smaller than the frequency in at least {n_comp_frequent} other plays (compared to the {n_remaining_plays} other plays by {st.session_state['author']}).
                """)
        higher=False
    
    st.divider()
    
    
    comp_df = lemma_comparison_with_remaining_plays(play_counts_for_comparison_df, st.session_state["play"], higher)
    significant_lemmas = identify_lemmas_with_higher_frequency_than_any_other_play(comp_df, n_remaining_plays, n_comp_frequent)
    significant_lemma_overview = lemma_stats_across_plays(st.session_state["all_lemmata_count_dfs"], significant_lemmas)
    
    st.markdown(f"""
              ### Comparatively {comp_type} lemmata
              """)
    
    st.markdown(""" """)
    pivot_df = create_pivot_table(significant_lemma_overview)
    st.data_editor(pivot_df, disabled=True)
    
    st.divider()
    
    bar_chart_comparison_of_selected_lemmas_all_plays(significant_lemma_overview)
    
    
    
        
    