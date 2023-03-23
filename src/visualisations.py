from src.helperFunctions import *


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

def bar_chart_comparison_of_selected_lemmas_all_plays(lemma_overview):
    
    
    barmode = st.radio("Stacked or grouped bars?", ["group", "stack"], horizontal=True)
    
    if barmode == "group": 
        error_bars_check = st.checkbox("Confidence Intervals?")
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