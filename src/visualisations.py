from src.helperFunctions import *


def speaker_to_verse_mapping_visual(selected_lemmata_text_df, remaining_selected_lemmata_text_df, play):
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
    
    fig.update_layout(
        margin=dict(pad=20, l=100),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title=dict(text="Verse")),
        title = dict(text=play, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig, use_container_width=True)