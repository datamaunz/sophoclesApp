from src.helperFunctions import *
import unicodedata as ud
import os

def strip_accents(s):
    return ''.join([c for c in ud.normalize('NFD', s) if ud.category(c) != 'Mn'])

@st.cache
def retrieve_play_names(author):
    #play_names = sorted([x.replace(".csv", "") for x in os.listdir(f'dataFiles/{author.lower()}/texts') if x not in [".DS_Store"]])
    play_names = [x.replace(".csv", "") for x in os.listdir(f'dataFiles/{author.lower()}/texts') if x not in [".DS_Store"]]
    return play_names

@st.cache
def get_lemmata_dfs_stacked(author, play_names):
    lemmata_count_dfs = []
    for play_name in play_names:    
        lemmata_count_df = pd.read_csv(f'dataFiles/{author.lower()}/lemmata_tables/{play_name}.csv')
        lemmata_count_df["play_name"] = play_name
        lemmata_count_dfs.append(lemmata_count_df)
    lemmata_count_df = pd.concat(lemmata_count_dfs)
    lemmata_count_df = lemmata_count_df[lemmata_count_df.lemma.isna() == False]
    lemmata_count_df["lemma_min"] = lemmata_count_df["lemma_min"].apply(lambda x: strip_accents(x))
    
    
    return lemmata_count_df.sort_values("lemma_min")
    #return lemmata_count_df



@st.cache
def load_play_text_df(author, selected_lemmata, play):
    text_df = pd.read_csv(f"dataFiles/{author.lower()}/texts/{play}.csv")
    text_df["selected_lemmata"] = text_df.lemmata.apply(lambda x: " ".join([lemma for lemma in str(x).split(" ") if lemma in selected_lemmata]))
    text_df["selected_lemmata"] = text_df["selected_lemmata"].apply(lambda x: None if x == "" else x)
    return text_df

@st.cache
def load_play_lemmata_count_df(author, play):
    lemmata_count_df = pd.read_csv(f"dataFiles/{author.lower()}/lemmata_tables/{play}.csv")    
    return lemmata_count_df