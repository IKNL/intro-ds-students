# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# Before we begin, we will change a few settings to make the notebook look a bit prettier

# %% {"language": "html"}
# <style> body {font-family: "Calibri", cursive, sans-serif;} </style>

# %% [markdown]
# <img src="https://github.com/IKNL/guidelines/blob/master/resources/logos/iknl_nl.png?raw=true" width=200 align="right">
#
# # 03 - Survival Analysis
#
# Perform some basic survival analysis on the synthetic data
#
# ## Imports

# %%

# %% [markdown]
# ## 3.1 Read the data
# Read the data file that you generated in the notebook `01_preprocessing`


# %%

# %% [markdown]
# ## 3.2 Kaplan-Meier analysis
# Perform a variety of KM analyses on the dataset. 
# Some pointers:
#
# * Calculate the duration (T) - the time to event (in our case, the event is either death or last time we contacted the patient)
# * Calculate the censorship (C)
# * Apply the KM fitter to the _whole_ dataset and generate KM curves
# * Now, generate KM curves to compare the survival depending on:
#     - Gender (male vs female) <br>
#       In this case, perform a log rank test: is the survival of males and females different?
#     - Clinical stage (numeric value)
#     - Pathological stage (numeric value)
#
# Make sure you save all your plots in the `results` directory
#
# **Tip**: take a look at [`lifelines`](https://lifelines.readthedocs.io/en/latest/)

# %%


# %% [markdown]
# ## 3.2 Cox Proportional Hazards analysis
# Perform a CPH analysis on the dataset. 
#
# * Make sure you process the variables accordingly (encoding, normalization, etc. where needed)
# * Generate a graphical representation of the coefficients
#
# Make sure you save all your plots in the `results` directory
#
# **Tip**: take a look at [`lifelines`](https://lifelines.readthedocs.io/en/latest/) (again)

# %%


# %% [markdown]
# * What do the coefficients of the regression tell us?
# * Which variable has the largest impact on survival?
# * What limitations does the CPH model have?

# %% [markdown]
# ...
