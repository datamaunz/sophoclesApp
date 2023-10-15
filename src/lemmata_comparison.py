from src.helperFunctions import *
import os




@st.cache_data
def lemma_stats_across_plays(all_lemmata_count_dfs, selected_lemmas):

    lemma_overview = all_lemmata_count_dfs[all_lemmata_count_dfs.lemma.isin(selected_lemmas)]
    lemma_overview = lemma_overview.sort_values("COUNT_perc", ascending=False)
    lemma_overview["error_down"] = lemma_overview["COUNT_perc"] - lemma_overview["LOW_perc"]
    lemma_overview["error_up"] = lemma_overview["HIGH_perc"] - lemma_overview["COUNT_perc"]
    return lemma_overview

@st.cache_data
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

@st.cache_data
def compute_counts_for_lemmas_in_plays(all_lemmata_count_dfs, play):
    play_counts = all_lemmata_count_dfs[all_lemmata_count_dfs.play_name == play]
    
    play_counts_basic = play_counts[["lemma", "COUNT", "LOW", "COUNT_perc", "LOW_perc", "HIGH", "HIGH_perc"]]
    play_counts_basic.columns = [f'{x}_{play}' for x in play_counts_basic.columns]
    
    non_play_counts = all_lemmata_count_dfs[(all_lemmata_count_dfs.play_name != play) & (all_lemmata_count_dfs.lemma.isin(play_counts.lemma.to_list()))]
    play_counts_for_comparison_df = pd.merge(non_play_counts, play_counts_basic, left_on="lemma", right_on=f"lemma_{play}")
    return play_counts_for_comparison_df





