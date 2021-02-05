# -*- coding: utf-8 -*-
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
# # 01 - Pre-processing
#
# Perform some pre-processing on the (synthetic) data
#
# **Important**: include all your imports here and here only.

# %%

# %% [markdown]
# ## 1.1 Read the data
# **Tip**: take a look at [`pandas read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

# %%

# %% [markdown]
# ## 1.2 Rename the columns
# Rename the columns of the original `DataFrame` as follows:
#
# | Original name | New name |
# |---------------|----------|
# | `rn`          | `nkr_id`   |
# | `zid`      | `disease_id`   |
# | `eid`      | `episode_id`   |
# | `gesl`      | `gender`   |
# | `gebdat`      | `birth_date`   |
# | `incdat`      | `incidence_date`   |
# | `topo`      | `topo`   |
# | `sublok`      | `sublocalization`   |
# | `topog`      | `topography`   |
# | `later`      | `lateralization`   |
# | `morf`      | `morphology`   |
# | `gedrag`      | `behaviour`   |
# | `diffgr`      | `grade`   |
# | `tumorsoort`      | `tumor_type`   |
# | `basisd`      | `diagnosis_basis`   |
# | `ct`      | `t_clin`   |
# | `cn`      | `n_clin`   |
# | `cm`      | `m_clin`   |
# | `pt`      | `t_patho`   |
# | `pn`      | `n_patho`   |
# | `pm`      | `m_patho`   |
# | `stadiumc`      | `stage_clin`   |
# | `stadium`      | `stage_patho`   |
# | `vitdat`      | `contact_date`   |
# | `ovldat`      | `death_date`   |
#
# This will make your code much easier to read (and more accessible to 
# non-Dutch speakers as well 😉).
#
# **Tip**: take a look at [`pandas rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html)
#
# As you get familiarized with the data, be sure to complete the table found in `../data/README.md`.

# %%

# %% [markdown]
# ## 1.3 Check data integrity
# Data are never perfect. Let's see how imperfect this dataset is.
#
# First, generate a visualization of the missing values.
#
# **Tip**: take a look at the [`missingno` package](https://github.com/ResidentMario/missingno)

# %%

# %% [markdown]
# How many missing values (in absolute numbers and as a percentage)
# are there for each column? Generate a bar plot showing this.

# %%

# %% [markdown]
# What methods do you know for dealing with missing values? 
# What are the advantages and disadvantages of each of them?

# %% [markdown]
# * ...

# %% [markdown]
# For now, we will keep it simple. Drop all the rows that contain missing data. How many records were lost because of this??

# %%

# %% [markdown]
# *In theory*, `topography` should be the concatenation of `topo` and
# `sublocalization`. For what number/percentage of records
# is this actually true?

# %%

# %% [markdown]
# ## 1.4 Feature engineering
# Let's make a small feature engineering. In all cases, make sure that you 
# only add these new features (i.e., columns) only if they aren't already present 
# in the `DataFrame`. 
#
# * Create a new column called `age_incidence`, which 
# contains the age of the patient at the moment of diagnosis. Use the 
# information contained in the columns `incidence_year` and `birth_date`. 


# %%


# %% [markdown]
# * Create two new columns called `stage_clin_num` and `stage_patho_num`. 
# Each of them will have the numerical part of the data contained
# in the columns `stage_clin` and `state_patho`, respectively.

# %%


# %% [markdown]
# * Create q new column called `death`, which has a `False` if the patient
# is still alive or a `True` if the patient already passed away.

# %%


# %% [markdown]
# ## 1.5 Decode features
# Many features in the NKR are encoded. While this will be useful later on,
# it can also make the data cryptic at this point.
#
# Decode the column `gender` as indicated in the following table
#
# | Original value | New value       |
# |----------------|-----------------|
# | 1              | `male`          |
# | 2              | `female`        |
# | 3              | `hermaphrodite` |
#

# %%


# %% [markdown]
# ## 1.6 Save the data
# Lastly, save the modified DataFrame as `df_preprocessing.csv` in the
# `data_processed` directory. 
#
# **Tip**: take a look at [`pandas to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)

# %%

# %% [markdown]
# Make sure that you generate a new section in the data `README.md` corresponding to this new data file. Remember to include information of the new features.
