import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a  wide range of plants specifically the leaves of the plants. "
        f"Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves and stems.\n"
        f"* Greenhouses provide an ideal moist, temperate environment for the spread of the disease. This causes harm to agricultural and horticultural practices where powdery mildew may thrive in a greenhouse setting.\n"
        f"* Cherry leaves are used and examined for this study. Visual criteria are used to detect the existence "
        f"of powdery mildew on the leaves. \n"
        f"* According to [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew), "
        f"Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. "
        f"Infected plants display white powdery spots on the leaves and stems."
        f" The lower leaves are the most affected, but the mildew can appear on any above-ground part of the plant.\n"
        f"* This disease can easily grow in environments with high humidity and moisture. \n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 cherry leaf images, of which 2104 are healthy, and the rest, 2104, "
        f" have powdery mildew."
        f" ")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Onursoyar/mildew-detection-cherry-leaves#readme).")

    st.header("Business Requirements")
    st.success(
        f"The project business requirementsare as follows:\n"
        f"* Analysis on average images and variability images for each class (healthy or powdery mildew).\n"
        f"* The differences between average healthy and average powdery mildew cherry leaves and an image montage for each class.\n"
        f"* Create and deliver an ML system which is able to predict if a cherry leaf is healthy or infected containing powdery mildew. \n"
    )
