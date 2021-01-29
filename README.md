<img src="https://github.com/IKNL/guidelines/blob/master/resources/logos/iknl_nl.png?raw=true" width=200 align="right">

Introduction to Data Science at IKNL<br> (for Students)
==============================

## Welcome to IKNL!
The purpose of this repository is to get you started with your project at IKNL.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── dissemination      <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── documents      <- Articles, written reports, etc.
    │      └── paper       <- LaTeX template for a paper
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── posters        <- Typically for conferences
    │   └── presentations  <- Usually PowerPoints (and their corresponding PDF)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── results            <- Intermediate/preliminary results (figures, variables, etc.).
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------

<p><small>Project based on <a target="_blank" href="https://github.com/iknl/cookiecutter-data-science-iknl">IKNL's Cookiecutter template for Data Science</a>.</small></p>
