# Practical Machine Learning for Physicists
> Welcome to the graduate course on machine learning at the Albert Einstein Center for Fundamental Physics of the University of Bern!


## What is this thing called machine learning?

<div style="text-align: center">
<img src="notebooks/images/machine_learning.png">
   <p style="text-align: center;"> <b>Figure reference:</b> https://xkcd.com/1838/ </p>
</div>

Machine learning is a subfield of artificial intelligence that focuses on using algorithms to parse data, learn from it, and then make predictions about something in the world. In the last decade, this framework has led to significant advances in [computer vision](https://www.youtube.com/watch?v=kSLJriaOumA&feature=youtu.be), [natural language processing](https://openai.com/blog/better-language-models/), and [reinforcement learning](https://openai.com/blog/emergent-tool-use/). More recently, machine learning has begun to attract interest in the physical sciences and is rapidly becoming an important part of the physicist's toolkit, especially in data-rich fields like high-energy particle physics and cosmology.

## Basics

**Timetable:** 14:15 to 16:00 on Tuesdays via Zoom due to the COVID-19 pandemic.

**Class Slack group:** [ml-for-physics.slack.com](https://ml-for-physics.slack.com)

If you need to contact me, I strongly encourage you to do so via Slack since I'll check this a few times per day.

## Learning objectives of the course
This course provides students with a _hands-on_ introduction to the methods of machine learning, with an emphasis on applying these methods to solve physics problems. By the end of this course, it is expected that students will:

* Know how to approach physics problems from a machine learning perspective;
* Understand the fundamental principles behind extracting useful knowledge from data; 
* Understand the core concepts and terminology of machine learning;
* Gain hands-on experience with mining data for insights.

Throughout the course, students will also have the opportunity to learn several technical skills:

* Python programming and experience with the core libaries for data analysis, visualisation, and modelling.
* Working with data: collecting, cleaning, and transforming.
* Creating and interpreting descriptive statistics.
* Creating and interpreting data visualisations.
* Practical experience with machine learning.

## Structure of the course
Due to constraints placed by the COVID-19 pandemic, the course will be delivered entirely via online lectures. Each lecture will involve a mix of theoretical and programming work, with an emphasis on the latter. A tentative outline for the course is shown in the table below. 

| CW | Date | Topic | Links |
| :--- | :--- | :--- | :--- |
| 15 | 7.4 | Introduction to random forests |  |
| 17 | 21.4 | Random forest deep dive |  |
| 18 | 28.4 | Model interpretation |  |
| 19 | 5.5 | Random forests from scratch | |
| 20 | 12.5 | Gradient boosting | |
| 21 | 19.5 | Topological machine learning I | |
| 22 | 26.5 | Topological machine learning II | |

## Cloud environment
We will be teaching most of the class via Jupyter notebooks in Python. You can open and run them directly on Binder by clicking on the Binder badge (see example below) at the top of each lecture notebook. We highly encourage the use of Binder, since it requires no local installation and runs for free. 

Binder badge:  ![Binder](https://mybinder.org/badge_logo.svg) 

A few remarks about Binder:

1. Binder is free to use.
2. If you edit a notebook make sure you _**download it**_, since Binder _**does not save your changes.**_
3. Binder will automatically shut down user sessions that have more than 10 minutes of inactivity (if you leave your browser window open, this will be counted as “activity”).
4. Binder aims to provide at least 12 hours of session time per user session. Beyond that, it is not guaranteed that the session will remain running.


### Downloading and uploading files
Since Binder does not save your changes permanently, you should download the notebooks you worked on at the end of your session. If you want to continue your session later on you can re-upload them to Binder. See the image below for instructions how to upload and download files.

<div style="text-align: center">
<img src="notebooks/images/binder-download-upload.png" width="800">
<p style="text-align: center;"> <b>Figure:</b> Download and upload buttons on JupyterLab as seen in the binder environment. </p>
</div>

## Local environment
You can also run the course material locally on your laptop. In general, when working with Python it is recommended to use [virtual environments](https://realpython.com/python-virtual-environments-a-primer/). This makes sure that the packages you install don't interfere with the packages you already installed in other projects.

To install the library associated with the course run the following command:

```bash
pip install hepml
```

To install JupyterLab (a more advanced environment than Jupyter notebooks) run:

```bash
pip install jupyterlab
```
Then make sure you download all course material from the [GitHub repository](https://github.com/lewtun/hepml) or just the missing notebooks. In general you will need to copy all materials, since some resources such as images are not self-contained in the notebooks.

Finally, to start JuypterLab run:
```bash
jupyter-lab
```

### Updating the local environment
Since we are developing the materials throughout the course you will need to update your local environment every time we move on to the next lesson. To do so just run the following command before you start JupyterLab

```bash
pip install --upgrade hepml
```

## Recommended references

**Machine Learning**
* J. Howard, [_Introduction to Machine Learning for Coders,_](https://course18.fast.ai/ml)
* P. Mehta et al., [_A high-bias, low-variance introduction to Machine Learning for physicists_](https://arxiv.org/abs/1803.08823)
* A. Géron, [_Hands-On Machine Learning with Scikit-Learn and TensorFlow,_](https://www.oreilly.com/library/view/hands-on-machine-learning/9781491962282/)
* J. Murugan and D. Robertson, [_An Introduction to Topological Data Analysis for Physicists: From LGM to FRBs_](https://arxiv.org/abs/1904.11044)

The structure of the lectures is adapted (with permission) from Jeremy Howard's excellent machine learning course for coders, while the theoretical content is based on the comprehensive review articles by Mehta et al and Murugan and Roberston.

**Python Programming**
* W. McKinney, [_Python for Data Analysis,_](http://shop.oreilly.com/product/0636920023784.do)

We will use the Python programming language to analyse and visualise a variety of datasets in this course. McKinney’s book is an excellent reference to have at hand and covers the nuts and bolts of the NumPy and pandas packages.

**Kaggle Learn**
* [Kaggle Learn](https://www.kaggle.com/learn/overview)

Kaggle Learn is a great resource to brush up on concepts like Python basics, data visualisation or pandas in an online notebook environment (similar to Binder).
