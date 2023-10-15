from src.helperFunctions import *
import unicodedata as ud
import os

def strip_accents(s):
    return ''.join([c for c in ud.normalize('NFD', s) if ud.category(c) != 'Mn'])

#@st.cache
@st.cache_data
def retrieve_play_names(author):
    #play_names = sorted([x.replace(".csv", "") for x in os.listdir(f'dataFiles/{author.lower()}/texts') if x not in [".DS_Store"]])
    #play_names = [x.replace(".csv", "") for x in os.listdir(f'dataFiles/{author.lower()}/texts') if x not in [".DS_Store"]]
    st.session_state["play_names"] = [x.replace(".csv", "") for x in os.listdir(f'dataFiles/texts_with_lemmas/{author.lower()}') if x not in [".DS_Store"]]
    return st.session_state["play_names"]
    

#@st.cache
@st.cache_data
def get_lemmata_dfs_stacked(author, play_names):
    lemmata_count_dfs = []
    for play_name in play_names:    
        #lemmata_count_df = pd.read_csv(f'dataFiles/{author.lower()}/lemmata_tables/{play_name}.csv')
        lemmata_count_df = pd.read_csv(f'dataFiles/lemma_tables/{author.lower()}/{play_name}.csv')
        lemmata_count_df["play_name"] = play_name
        lemmata_count_dfs.append(lemmata_count_df)
    lemmata_count_df = pd.concat(lemmata_count_dfs)
    lemmata_count_df = lemmata_count_df[lemmata_count_df.lemma.isna() == False]
    lemmata_count_df["lemma_lower"] = lemmata_count_df["lemma_lower"].apply(lambda x: strip_accents(x))
    
    return lemmata_count_df.sort_values("lemma_lower")
    #return lemmata_count_df

@st.cache_data
def get_play_lemmata_versus_non_play_lemmata(all_lemmata_count_dfs, play):
        play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title == play]
        non_play_lemmata_df = all_lemmata_count_dfs[all_lemmata_count_dfs.title != play]
        return play_lemmata_df, non_play_lemmata_df

#@st.cache
@st.cache_data
def load_play_text_df(author, selected_lemmata, play):
    #text_df = pd.read_csv(f"dataFiles/{author.lower()}/texts/{play}.csv")
    text_df = pd.read_csv(f'dataFiles/texts_with_lemmas/{author.lower()}/{play}.csv')
    text_df["selected_lemmata"] = text_df.Lemmas.apply(lambda x: " ".join([lemma for lemma in str(x).split(" ") if lemma in selected_lemmata]))
    text_df["selected_lemmata"] = text_df["selected_lemmata"].apply(lambda x: None if x == "" else x)
    return text_df

#@st.cache
@st.cache_data
def load_play_lemmata_count_df(author, play):
    lemmata_count_df = pd.read_csv(f"dataFiles/{author.lower()}/lemmata_tables/{play}.csv")    
    return lemmata_count_df