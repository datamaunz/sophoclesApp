from src.helperFunctions import *
import os

@st.cache
def comparison_of_play_to_others_for_selection(play_lemmata_df, non_play_lemmata_df, selected_lemmata, play_names, play):
    
    play_lemmata_selection_df = play_lemmata_df[play_lemmata_df.lemma.isin(selected_lemmata)]
    play_lemmata_stats = pd.DataFrame(play_lemmata_selection_df[["MIN_perc", "LOW_perc", "COUNT_perc", "HIGH_perc", "MAX_perc"]].sum()).T
    play_lemmata_stats.columns = [f'{x} {play}' for x in play_lemmata_stats.columns]
    non_play_lemmata_selection_df = non_play_lemmata_df[non_play_lemmata_df.lemma.isin(selected_lemmata)]
    
    no_counts_names = [x for x in play_names if x not in list(non_play_lemmata_selection_df.title.unique()) + [play]]
    non_play_lemmata_stats = non_play_lemmata_selection_df.groupby("title")[["MIN_perc", "LOW_perc", "COUNT_perc", "HIGH_perc", "MAX_perc"]].sum()
    for no_counts_name in no_counts_names:
        non_play_lemmata_stats = pd.concat([non_play_lemmata_stats, pd.DataFrame({column_name:[0] for column_name in ["MIN_perc", "LOW_perc", "COUNT_perc", "HIGH_perc", "MAX_perc"]}, index=[no_counts_name])])
    
    for column in play_lemmata_stats.columns:
        non_play_lemmata_stats[column] = play_lemmata_stats[column].iloc[0]
    
    non_play_lemmata_stats["significant HIGH"] = non_play_lemmata_stats[f"HIGH_perc"] < non_play_lemmata_stats[f"COUNT_perc {play}"]
    non_play_lemmata_stats["significant LOW"] = non_play_lemmata_stats[f"LOW_perc"] > non_play_lemmata_stats[f"COUNT_perc {play}"]
    
    non_play_lemmata_stats["RATIO"] = round(non_play_lemmata_stats[f"COUNT_perc {play}"] / non_play_lemmata_stats[f"COUNT_perc"], 1)
    
    return play_lemmata_stats, non_play_lemmata_stats 