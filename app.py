
from src.helperFunctions import *

def main():
    
    primaryColor="#ef3340"
     
    st.set_page_config(
        layout="wide",
        page_title="Ben's App",
        page_icon = "🏹"
        )

    df = readInFile("dataFiles/tables/oedipusAtColonus_mainFrame.csv")
    
    lemmaDf = readInFile("dataFiles/tables/oedipusAtColonus_lemmataFrame.csv")

    uniqueLemmata = sorted(lemmaDf.lemma.unique())

    selectedWords = st.sidebar.multiselect("Select lemmata", uniqueLemmata)
    
    selectedWordDf = createSelectedWordDf(lemmaDf, selectedWords)


    createOverviewFigure(df, selectedWordDf)
    
if __name__ == '__main__':
    main()
    