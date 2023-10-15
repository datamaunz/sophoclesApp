import streamlit as st
import plotly.express as px

from src.lemmata_comparison import lemma_stats_across_plays


def bar_chart_comparison_of_selected_lemmas_all_plays(lemma_overview):
    
    col1, col2 = st.columns(2)
    
    barmode = col1.radio("Stacked or grouped bars?", ["group", "stack"], horizontal=True)
    
    if barmode == "group": 
        col2.markdown(""" """)
        error_bars_check = col2.checkbox("Confidence Intervals?")
    else: error_bars_check = None
    
    if barmode == "group":
        if error_bars_check == True:
            fig = px.bar(lemma_overview, x="title", y="COUNT_perc", color="lemma", error_y="error_up", error_y_minus="error_down", barmode=barmode, text="COUNT")
        else:
            fig = px.bar(lemma_overview, x="title", y="COUNT_perc", color="lemma", barmode=barmode, text="COUNT")
        
    else:
        fig = px.bar(lemma_overview, x="title", y="COUNT_perc", color="lemma")
    fig.update_layout(
        xaxis=dict(title=""),
        yaxis=dict(title="lemma frequency"),
    )
    st.plotly_chart(fig, use_container_width=True)


def display_page_2():
    st.session_state["lemma_overview"] = lemma_stats_across_plays(st.session_state["all_lemmata_count_dfs"], st.session_state["selected_lemmas"])
    bar_chart_comparison_of_selected_lemmas_all_plays(st.session_state["lemma_overview"])