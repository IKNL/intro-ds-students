<img src="https://github.com/IKNL/guidelines/blob/master/resources/logos/iknl_nl.png?raw=true" width=200 align="right">

# Introduction to Data Science at IKNL<br> (for Students)

## Welcome to IKNL!
The purpose of this repository is to get you familiarized with the tools that you will be using during your time at IKNL.

## Getting your setup up and running
This should help you get your setup up and running.

1. #### Install Anaconda <br>
  Anaconda is a great all-in-one solution for Data Science. I recommend you install it from [here](https://www.anaconda.com/products/individual)

2. #### Create an environment <br>
  An environment is basically a sandbox where you can install all the packages that you want for a specific project. The advantage is that you can have several, independent environments. For example, you can have one environment for your Python course, one for your internship, etc. These would be completely independent (e.g., if you install one package for your Python course, that doesn’t mean it will be installed in your internship environment).
  * In the Windows start menu, look for `Anaconda Prompt`
  * Right click on it and select `Run as administrator`
  * In the console, type <br>
     `conda create -n iknl-internship` <br>
     This will create an environment called `iknl-internship`. You can, of course, choose whichever name you want.
   * Now type <br>
      `conda activate iknl-internship`
      You will see that the console reflects that you are now working on `iknl-internship`.
   * You can check what packages you have installed in your environment with <br>
      `conda list`

This are just the basics for creating an environment. You can take a look at the [complete documentation here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

From now on, I recommend that for every package that you want to install, always look for the `conda` version (there is another alternative which is using `pip`; however, I don’t recommend using it unless it is the only option, since that could break your `conda` environment – sometimes `conda` and `pip` don’t like each other).

3. #### Install Spyder <br>
  We will now install [Spyder](https://www.spyder-ide.org/). It is my favorite integrated development environment (or IDE). Moreover, it is open source! You can do so with the command

  `conda install -c anaconda spyder`

  Check that Spyder installed correctly (`conda list`). Then, launch it in console with

  `spyder &`

Notice that this will “block” your current console. So from now on, if you wish to use it, you will need to open a new one (same steps, including running it as admin). Don’t forget to activate the right environment!

4. #### Install Jupyter Notebook <br>
Jupyter Notebook allows you to create - well - notebooks to show your work. They are a great option to combine text (using Markdown) and code in a single file, which makes them great for sharing. Install it with the command

  `conda install -c conda-forge notebook`

  Check that it was installed correctly (`conda list`). Then, make sure that you are in the right directory (probably your project's root directory) and start it in console with

  `jupyter notebook`

This will launch a session in your preferred web browser. Notice that this will “block” your current console. Similarly as before, you will need to open a new one (same steps, including running it as admin). Don’t forget to activate the right environment!

5. #### Install Jupytext <br>
The next thing would be [Jupytext](https://github.com/mwouts/jupytext), a tool that allows you to save Jupyter notebooks as plain `.py` files (in other word, sync them). This way, you can edit them in your preferred IDE (in our case, Spyder). More importantly, this makes version control on them much more manageable. Install it by typing

  `conda install jupytext -c conda-forge`

Now, when you open a Jupyter notebook, go to `File` --> `Jupytext` and check the option `Pair Notebook with percent Script`. This will create an accompanying `.py` file to your notebook. From now on, changes that you make in one will be reflected on the other. For more information, take a look at its [documentation](https://jupytext.readthedocs.io/en/latest/).

6. #### Install Git (and setup GitHub) (and clone this repository) <br>
Finally, install Git, a powerful tool for version control. You can do so for Windows [here](https://git-scm.com/download/win) (classic installation, no console this time).

Create a [GitHub](https://github.com/) account (if you don't have one already) and set it up with Git. You can follow [GitHub's comprehensive documentation](https://docs.github.com/en/github/getting-started-with-github/set-up-git) or any [other tutorial](https://kbroman.org/github_tutorial/pages/first_time.html) that you might find.

If you aren't familiarized with Git, I recommend you follow this [cute online tutorial](https://learngitbranching.js.org/). I like it because is shows you graphically what’s happening. Moreover, it mimics the experience of working on the terminal very well. Additionally, you cannot mess stuff there. At the beginning, Git might look very complicated. Take it easy. Although it has a learning curve, in the end it will prove very useful for your project.

7. #### Get started!
Now, clone this repository by opening a Git console and typing

  `git clone git@github.com:IKNL/intro-ds-students.git`

Go to the `notebooks` directory and get started. Good luck 🍀!

  ### Project organization

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
      ├── notebooks          <- You will find your exercises here.
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


## References
* [Managing environments with `conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Jupytext documentation](https://jupytext.readthedocs.io/en/latest/)
* [Setting up Git with GitHub](https://docs.github.com/en/github/getting-started-with-github/set-up-git)
* [Practical online Git tutorial](https://learngitbranching.js.org/)

--------
<p><small>Project based on <a target="_blank" href="https://github.com/iknl/cookiecutter-data-science-iknl">IKNL's Cookiecutter template for Data Science</a>.</small></p>
