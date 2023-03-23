import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def lineBreaksForString(string, n):
    wordList = string.split(" ")
    lines = int(np.ceil(len(wordList) / n))
    
    lineList = []
    for i in range(lines):
        lineList.append(" ".join(wordList[i*n:(i+1)*n]))
    return "<br>".join(lineList)    

#@st.cache(suppress_st_warning=True, show_spinner=False)
def createOverviewFigure(df, selectedWordDf):
    
    fig = go.Figure()

    for index, row in df.iterrows():
        fig.add_traces(go.Scatter(
            x = [row.start, row.end], 
            y = [row.speaker, row.speaker],
            #marker = dict(color="grey", opacity=0.1),
            marker = dict(color="rgba(10,10,10,0.3)"),
            line=dict(width = 20),
            #customdata = [[lineBreaksForString(row.text, 15)]],
            customdata = [[lineBreaksForString(row.text, 10)]],
            hovertemplate="%{customdata[0]}",
            #mode="markers"
            mode="lines",
            showlegend=False
        ))


    if len(selectedWordDf) == 0:
        pass
    else:
        words = selectedWordDf.lemma.unique()
        for word in words:
            subTelDf = selectedWordDf[selectedWordDf.lemma == word]
            

            fig.add_traces(go.Scatter(
                x = subTelDf.wordCount, 
                y = subTelDf.speaker,
                name = word,
                #marker = dict(color="grey", opacity=0.1),
                marker = dict(size=10),
                #line=dict(width = 20),
                mode="markers",
                
                #mode="lines",
                #showlegend=False
            ))

    fig.update_layout(
        margin=dict(pad=20, l=100),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)

#@st.cache(suppress_st_warning=True, show_spinner=False)    
@st.cache_data
def readInFile(path):
    return pd.read_csv(path)

#@st.cache(suppress_st_warning=True, show_spinner=False)    
@st.cache_data
def createSelectedWordDf(lemmaDf, selectedWords):
    return lemmaDf[lemmaDf.lemma.isin(selectedWords)]