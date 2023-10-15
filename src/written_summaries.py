from src.helperFunctions import *

def write_comparison_in_words(non_play_lemmata_stats, selected_lemmata, play):
        
    st.markdown(f"### Comparison")
    st.write("")

    more_frequent_than = non_play_lemmata_stats[non_play_lemmata_stats["significant HIGH"]][["RATIO"]]
    more_frequent_than_in = [f"{index} ({row.RATIO} times)" for index, row in more_frequent_than.iterrows()]
    not_more_frequent_than = non_play_lemmata_stats[non_play_lemmata_stats["significant HIGH"] == False][["RATIO"]]
    not_more_frequent_than_in = [f"{index} ({row.RATIO} times)" for index, row in not_more_frequent_than.iterrows()]
    
    if len(selected_lemmata) > 0:
    
        st.markdown(f"""In **{play}** the selected group of lemmata is *significantly more frequent* than in""")
        for item in more_frequent_than_in:
                st.markdown(f"""- {item}""")
        
        if len(not_more_frequent_than_in) > 0:
            st.markdown("""It is not *significantly more frequent* than in""")
            for item in not_more_frequent_than_in:
                st.markdown(f"""- {item}""")

def write_comparison_in_words(non_play_lemmata_stats, selected_lemmata, play):
    
    significance_dict = {False:'insignificant', True:'significant'}
        
    st.markdown(f"### Comparison")
    st.write("")

    more_frequent_than = non_play_lemmata_stats[non_play_lemmata_stats["RATIO"] > 1].sort_values("RATIO", ascending=False)
    more_frequent_than_in = [f"{index} ({row.RATIO} times; *{significance_dict.get(row['significant HIGH'])}*)" for index, row in more_frequent_than.iterrows()]
    
    not_more_frequent_than = non_play_lemmata_stats[non_play_lemmata_stats["RATIO"] <= 1].sort_values("RATIO", ascending=True)
    not_more_frequent_than_in = [f"{index} ({row.RATIO} times; *{significance_dict.get(row['significant LOW'])}*)" for index, row in not_more_frequent_than.iterrows()]
    
    if len(selected_lemmata) > 0:
        
        if len(more_frequent_than) > 0:
    
            st.markdown(f"""In **{play}** the selected group of lemmata is **more frequent** than in""")
            for item in more_frequent_than_in:
                    st.markdown(f"""- {item}""")
        
        st.markdown(f""" """)
        
        if len(not_more_frequent_than_in) > 0:
            st.markdown(f"""In **{play}** the selected group of lemmata is **less frequent** than in""")
            for item in not_more_frequent_than_in:
                st.markdown(f"""- {item}""")
