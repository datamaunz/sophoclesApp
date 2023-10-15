import streamlit as st
import plotly.graph_objects as go
from src.datafile_selection import load_play_text_df


def speaker_to_verse_mapping_visual(selected_lemmata_text_df, remaining_selected_lemmata_text_df, play):
    color_per_lemma = st.checkbox("one color per lemma", True)
    fig = go.Figure()
    
    fig.add_traces(go.Scatter(
        x = remaining_selected_lemmata_text_df.inferred_verse_number,
        y = remaining_selected_lemmata_text_df.Name,
        marker = dict(color="rgba(10,10,10,0.3)"),
        customdata = [[x] for x in remaining_selected_lemmata_text_df.Speech],
        hovertemplate="%{customdata[0]}",
        mode="markers",
        showlegend=False,
        name=""
    ))
    
    if color_per_lemma == False:
    
        fig.add_traces(go.Scatter(
            x = selected_lemmata_text_df.inferred_verse_number,
            y = selected_lemmata_text_df.Name,
            marker = dict(color="red"),
            customdata = [[x] for x in selected_lemmata_text_df.Speech],
            hovertemplate="%{customdata[0]}",
            mode="markers",
            showlegend=False,
            name=""
        ))
    
    else:
        
        unique_lemmata = selected_lemmata_text_df.selected_lemmata.unique()
        for lemma in unique_lemmata:
            frame = selected_lemmata_text_df[selected_lemmata_text_df.selected_lemmata == lemma]
            
            fig.add_traces(go.Scatter(
                x = frame.inferred_verse_number,
                y = frame.Name,
                #marker = dict(color="red"),
                customdata = [[x] for x in selected_lemmata_text_df.Speech],
                hovertemplate="%{customdata[0]}",
                mode="markers",
                showlegend=True,
                name=lemma))
            
    fig.update_layout(
        margin=dict(pad=20, l=100),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title=dict(text="Verse")),
        title = dict(text=play, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig, use_container_width=True)

@st.cache_data
def show_verses_with_lemmata(selected_lemmata_text_df):
    
    st.markdown(f"### Examples")
    st.write("")

    for index, row in selected_lemmata_text_df.iterrows():
        st.markdown(f"""**{row.Name}**: {row.Speech} ({str(int(row.inferred_verse_number))})""")


def display_page_1():
    st.session_state["text_df"] = load_play_text_df(st.session_state["author"], st.session_state["selected_lemmas"], st.session_state["play"])
    st.session_state["selected_lemmata_text_df"] = st.session_state["text_df"][st.session_state["text_df"].selected_lemmata.isna() == False]
    st.session_state["remaining_selected_lemmata_text_df"] = st.session_state["text_df"][st.session_state["text_df"].selected_lemmata.isna() == True]
    speaker_to_verse_mapping_visual(st.session_state["selected_lemmata_text_df"], st.session_state["remaining_selected_lemmata_text_df"], st.session_state["play"])      
    
    if len(st.session_state["selected_lemmata_text_df"]) > 0:
        st.markdown("---")
        show_verses_with_lemmata(st.session_state["selected_lemmata_text_df"])