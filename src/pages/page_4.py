import streamlit as st


def display_page_4():

    
    
    st.markdown(
        "### Data"
    )
    st.markdown(
        "The texts have been obtained from [Perseus](http://www.perseus.tufts.edu/hopper/)."
    )
    
    st.markdown(
        "### Lemmatization"
    )
    
    st.info("""
            A *lemma* is the dictionary/citation form of a set of word forms.
            """)
    
    st.markdown(
        """None of the existing lemmatizers delivered satisfactory results.
        To make sure this analysis is based on the best available information,
        we scraped the highest ranked lemma for every word directly from Perseus.
        We believe that lemmatizers should work as sequence to sequence models.
        If you'd like to cooperate on that, please get in touch."""
    )
    
    st.markdown(
        "### Confidence Intervals"
    )
    
    st.info("""
            In this study, bootstrapping confidence intervals for lemma frequencies in Sophocles’
            plays serves to estimate the range in which normal lemma frequencies occur,
            based on each individual play’s style. By applying bootstrapping, a statistical resampling method,
            numerous samples of lemma frequencies are generated to create confidence intervals.
            These intervals help in assessing whether observed variations in lemma frequencies
            between different plays are statistically significant or simply occur by chance.
            In essence, this analysis aids in distinguishing genuine stylistic differences
            from random variations in the use of words across Sophocles' works.
            """)
    
    st.markdown(
        """
        [Bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) confidence intervals is a statistical technique that involves
        generating many simulated datasets by randomly selecting samples with replacement from the original dataset (in this case, 1000 samples per play).
        By repeatedly calculating a statistic of interest (in this case, word frequencies) for each simulated dataset, 
        we can estimate the distribution of the statistic and use it to calculate the confidence interval.

        The [confidence interval](https://en.wikipedia.org/wiki/Confidence_interval) is a range of values that we can be reasonably
        sure contains the true value of the statistic in the population.
        The bootstrapped confidence interval is often more accurate than traditional methods
        because it accounts for the variability in the data and does not rely on assumptions about the population distribution.
        
        Note the assumption underlying our approach: In contrast to standard use cases of bootstrapping,
        we do know the true frequency of all words in all plays.
        The bootstrapped confidence intervals are used to simulate the distribution
        of word frequencies that can be expected for any play written in this particular style.
        """

    )
    
    st.markdown(
        "### Contributors"
    )
    
    st.markdown(
        """
        - [**Ben Folit-Weinberg**](https://research-information.bris.ac.uk/en/persons/benjamin-folit-weinberg): Principal Investigator
        - [**Justus Schollmeyer**](https://www.linkedin.com/in/justus-schollmeyer-014a2314b/): Creation of the app and methodology
        - [**Tom Odhiambo**](https://www.linkedin.com/in/tom-odhiambo/): Work on sequence to sequence model for improved lemmatization"""
    )
    
    st.markdown(
        """
        ### Github Repo
        
        The Github repository of the project can be found [here](https://github.com/datamaunz/sophoclesApp).
        """
    )
    
    st.markdown(
        "### Acknowledgement"
    )
    st.markdown(
        "We are grateful for the funding of the project by:"
    )
    
    col1, col2, col3 = st.columns(3)
    col1.image('dataFiles/images/Sophocles_funders.001.jpeg', caption="The Jean Golding Institute", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    col2.image('dataFiles/images/Sophocles_funders.002.jpeg', caption="The A.G. Leventis Foundation", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    col3.image('dataFiles/images/Sophocles_funders.003.jpeg', caption="The British Academy", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")