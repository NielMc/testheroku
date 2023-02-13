
# Mildew Detection in Cherry Leaves

********************
## Introduction
********************


 The customer working for a company in the agricultural sector  is in need and looking for a more efficient and simple method to sort out and process if their crops have been infected with Mildew or not. The active method that they are using is to manually go through and inspect the cherry leaves on their site. This method is both costly and consumes a huge amount of time.
 They purpose of this project will be to simplfy their work through creating a predictive analysis machine learning tool which will be able to inspect and assess the leaf pictures uploaded within a very short amount of time and confirm whether it is infected or healthy. 



********************
## Business Requirements
********************

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

********************
## The Dataset
********************
* The dataset is sourced from Kaggle. We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.

* The dataset contains more than 4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

********************
## Hypothesis and Validation
********************

*  The infected cherry leaves with powdery mildew have white streaks on surface. 

* The infected cherry leaves with powdery mildew have white streaks on surface which makes them visually different than of the healthy cherry leaves.

* The developed ML image visualizer will be able to divide and differentiate a healthy cherry leaf and an infected one.

* The ML image visualizer can help quickly and easily differentiate between images, which can save  time and money during inspections.

* The image visualizer has an accuracy rate of 97% which makes it fast, efficient and simple.


********************
## ML Tasks and Data visualizations Rationale
********************

* Business Requirement 1: The company is wants to conduct a study to visually differentiate a cherry leaf that is healthy from an infected one'

   * It will display the "mean" and "standard deviation" images for healthy and infected leaves.
   * It will display the difference between an average leaf with powdery mildew and an average healthy cherry leaf.
   * It will display a image montage for either healthy or diseased leaves.

* Business Requirement 2: The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.

   * It will need to predict if a given sample is diseased with powdery mildew or not.
   * Build a binary classifier and generate reports

********************
## ML Business Case
********************

* The idea of the business is to create a study to visually differentiate cherry leaves between healthy and diseased with powdery mildew to a degree of 97% accuracy.

* The ideal outcome is to provide the business a reliable and high accuracy in predicting healthy or diseased cherry crop by using sample leaves.

* The output is reflected in a dashboard using streamlit and the team working in the business can easily upload images of a sample cherry leaf. It reduces the manual processes around predicting powdery mildew in the plantation.

* The data analysis method can be used to visually inspect and differentiate these images of the leaves in order sort if the image contains a healthy or infected leaf.


********************
## Dashboard Design
********************
#### Streamlit was used for the project dashboard. It has a responsive design with a menu located on the left part of the page. These are the following:

*  Quick Project Summary
* Cherry Leaves Visualizer
* Mildew Detection
* Project Hypothesis
* ML Performance Metrics



********************
## Deployment
********************


### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


********************
## Data Analysis and Machine Learning Libraries
********************

* [Jupyter notebooks](https://jupyter.org/) the main source  for running and executing the ML pipelines.

* [Streamlit](https://streamlit.io/) is used to host the interactive dashboard.

* [Pandas](https://pandas.pydata.org/) is used for data analysis, especially for structuring the data.

* [Numpy](https://numpy.org/) is used to handle and manipulate multi-dimensional arrays, including providing a wide set of mathematical functions to operate on those arrays.

* [Matplotlib](https://matplotlib.org/) is used for data visualization including embedding plots in Jupyter notebooks.

* [Plotly](https://plotly.com/) is used for plotting data, functions, and to add animation to data visualization.

* [Scikit-learn](https://scikit-learn.org/stable/) contains tools used for data processing, predictive analysis, specifically used in this case to train the machine learning models for classification.

* [Seaborn](https://seaborn.pydata.org/) is a high-level interface for statistical graphics and it offers numerous built-in themes for styling Matplot graphics.

* [Tensorflow](https://www.tensorflow.org/) is used to filter out corrupt images or missing data during image processing.

* [Keras](https://keras.io/) was used for the CNN model for the ML pipeline.

* [Joblib](https://joblib.readthedocs.io/en/latest/) was used for loading and saving the images shapes.

* [Github](https://github.com/) is used for hosting the project and accepting all of the pushed code.

* [Gitpod](https://github.com/) is the workspace that hosted all facets of the project.

* [Heroku](https://heroku.com) was used for deployment of the project.

********************
## Credits 
********************


- Assistance and support for this project came in two main groups: **content** and **data/images**. Below, you'll find siting’s for both groups and links to each source:


********************
## Content 

* [Code Institute Malaria Walk Through Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/) was heavily used for instructional purposes, and guidance through the development of this project.
* [Code Institute Streamlit lessons](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/fc2f9892cfa44eee9cc8bf585c21df88/4?activate_block_id=block-v1%3Acode_institute%2BCI_DA_ML%2B2021_Q4%2Btype%40vertical%2Bblock%407636b337caeb4035bd7b5568404802f6) was used as guidance for the dashboard execution in this project.

* [Mildew Detection](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) was forked to provide the base foundation of this project.


* [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew#:~:text=Powdery%20mildew%20is%20a%20fungal,its%20symptoms%20are%20quite%20distinctive.) was used as the resource pertaining to the powdery mildew fungal infection that is at the heart of this project.

* [GyanShashwat1611/WalkthroughProject01](https://github.com/GyanShashwat1611/WalkthroughProject01) github repository was used for code reference and assistance for in the jupyter notebook set up, code and execution; as well as for the app pages design, set up and code

* [valerieoni/mildew-detection](https://github.com/valerieoni/mildew-detection) github repository was used for readme guidance and code reference. 

* [jtm2021/mildewproject](https://github.com/jtm2021/mildewproject) github repository was used for code reference and readme guidance

* [HaimanotA/Instant-Mildew-Detector](https://github.com/HaimanotA/Instant-Mildew-Detector) github repository was used for code reference and readme guidance

* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)


********************
## Acknowledgements
* I would like to thank my mentor ofr his help and motivation. I ahve taken inspiration from the walktrough project 1 and created this project.