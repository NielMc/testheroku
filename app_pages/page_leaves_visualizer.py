import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaves_visualizer_body():
    st.write("### Detection of Mildew in leaves")
    st.info(
        f" Within this page you can see that differences between an infected leaf with **powdery mildew** "
        f"and a **healthy** one.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_var_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            f" As we inspect closely we notice a difference in the colors of the leaves and"
            f" the patterns where we could intuitively differentiate one to another."
            f" A healthy leaf has a more dark green color while an infected leaf has a more light and white patterned surface. ")

        st.image(avg_powdery_mildew,
                 caption='Healthy leaf- Average and Variability')
        st.image(avg_var_healthy,
                 caption='Infected powdery mildew leaf- Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average infected and average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"The dark image at the end is the comparison between the two types(healthy and infected)."
            f"With the patterns we can almost differentiate one to another.")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"):
        st.write(
            "Click the 'Create Montage' button to create and refresh the image montage.")
        my_data_dir = 'inputs/cherry_leaves/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if the montage space is greater than subset size
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
