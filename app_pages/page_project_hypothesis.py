import streamlit as st


def page_project_hypothesis_body():

    st.header(" Hypothesis of the Mildew detection in cherry leaves ")

    st.info(
        f"The main hypotheses for this project are as follows:\n\n "

        f" The infected cherry leaves with powdery mildew have white streaks on surface "
        f"    which makes them visually different than of the healthy cherry leaves.\n\n"
        f" The developed ML image visualizer will be able to divide and differentiate a healthy cherry leaf and an infected one.\n"

    )
    st.success(
        f" While the infected mildew leaves show a lighter signs on the surface, the healthy ones show a much more darker color on its surface.\n\n "
        f" The leaves are a bit round, powders looking patches on young, susceptible leaves (light green expanding leaves) that can differentiate, from healthy ones. \n\n"
        f" The image validator will be able to differentiate between a healthy and infected cherry leaf.\n\n"

    )
