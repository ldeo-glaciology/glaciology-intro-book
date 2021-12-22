#!/usr/bin/env python
# coding: utf-8

# # Binder for Reproducible Research
# 
# This lecture is concerned with the topic of reproducibility.
# Nearly everyone agrees that reproducibility is an important principle for science:
# if results are not reproducible, they are not valid.
# 
# But how do we achieve reproducibility in practice?
# In computational / data science, a particular analysis, calculation, or notebook may depend on hundreds of different software packages, each with many different versions.
# Reproducibility of our results depends on having the correct version.
# 
# In the [lesson on python environments]({filename}/Lectures/python_environments.md), we learned how to use [conda](https://conda.io/docs/) to manage the packages in our environment.
# In this lesson, we will learn how to package our own code / notebooks together with an environment in such a way that it can be executed by anyone / anywhere, using cloud computing.
# 
# ![Binder Logo](https://mybinder.org/static/logo.svg)
# 
# 
# From the [Binder Documentation](https://mybinder.readthedocs.io/en/latest/)
# 
# > Binder allows you to create custom computing environments that can be shared and used by many remote users. It is powered by [BinderHub](https://github.com/jupyterhub/binderhub), which is an open-source tool that deploys the Binder service in the cloud. One-such deployment lives ... at mybinder.org and is free to use.
# 
# BinderHub uses a combination of open source technologies, including JupyterHub and [Docker](https://docs.docker.com/) (a containerization service), to achieve this magic.
# 
# In addition to the <http://mybinder.org> deployment, the Pangeo project operates a BinderHub service at <http://binder.pangeo.io>. This BinderHub is customized to allow users to also launch Dask clusters in the cloud.
# 

# ## An Example Binder
# 
# All binders start with a github repository. As an example, let's consider the the official dask examples repo: <https://github.com/dask/dask-examples>
# 
# ### Contents
# 
# The repository should contain the following two elements:
# 
# - Python code and / or notebooks (these can live in sub-directories)
# - An `environment.yml` or `requirements.txt` file to specify the package dependencies (can be at the top level or in a subdirectory called `binder/`)
# 
# The dask-examples repo contains about 10 different example notebooks.
# 
# To specify the environment, the dask-example repo has the following file at `binder/environment.yml`
# 
# ```
# name: dask-examples
# channels:
#   - conda-forge
# dependencies:
#   - python=3.8
#   - bokeh=2.1.1
#   - dask=2.20.0
#   - dask-image=0.2.0
#   - dask-ml=1.6.0
#   - dask-labextension=2.0.2
#   - jupyterlab=2.1
#   - nodejs=14
#   - numba
#   - numpy=1.21
#   - pip
#   - pandas=1.3
#   - pyarrow
#   - python-graphviz
#   - seaborn
#   - scikit-learn=0.23
#   - matplotlib
#   - nbserverproxy
#   - nomkl
#   - h5py
#   - xarray
#   - pooch
#   - bottleneck
#   - requests
#   - py-xgboost
#   - dask-xgboost
#   - pip:
#       - mimesis
#       - pystan==2.19.1.1
#       - prophet
# ```
# 
# This is a rather complex set of dependencies.
# In addition, there are other files in the `binder/` directory that help further customize the environment.
# These customizations are described in the [Binder Documentation](https://mybinder.readthedocs.io/en/latest/using.html#executing-post-build-commands).
# 
# ### Binder Link
# 
# Once the repository is ready, it's time to generate a link to the BinderHub.
# These links have the following structure:
# 
#     https://mybinder.org/v2/<provider-name>/<org-name>/<repo-name>/<branch|commit|tag>?filepath=<path/to/notebook.ipynb>
#     
# For the dask-examples repo, the link used is:
# 
#     https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab
#     
# In this case, `provider` is `gh` (i.e. github).
# 
# The <https://mybinder.org/> website has a nifty tool to automatically generate badges that can be placed on a website or markdown file to make it easy to launch the binder.
# For dask-examples, the markdown code looks like this:
# 
# `[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab)`
# 
# And renders like this
# 
# [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab)
# 
# Take some time to launch the binder and play around with it.

# ## nbgitpuller tricks
# 
# The original binder model kept both the code itself and the environment specification in the same repo.
# The way binder works means that _every time the repo is updated, the environment must be completely rebuilt from scratch._
# As we have seen, building a complex python environment can take upwards of 20 minutes. 
# So even if you only change a comment in your code, the entire environment is rebuilt when you try to relaunch the binder.
# Users usually update their code much more frequently than they update the environment.
# Furthermore, many binders may want to share the _same_ base environment.
# 
# To address these issues, we can leverage a clever tool called [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/).
# Nbgitpuller is a JupyterHub extension that allows you to automatically launch content from a github repo into a specific
# JupyterHub or Binder via a simple URL.
# That's how this book works.
# The "Launch JupyterHub" button for this page points to the following link:
# 
# ```
# https://https//us-central1-b.gcp.pangeo.io//hub/user-redirect/git-pull?repo=https://github.com/earth-env-data-science/earth-env-data-science-book&urlpath=lab/tree/earth-env-data-science-book/src/lectures/environment/binder.ipynb&branch=master
# ```
# 
# Ok, maybe not a "simple" URL. 😬 In fact, constructing these links can be so tricky that nbgitpuller has a [special webpage](https://jupyterhub.github.io/nbgitpuller/link.html) to help you generate them.
# 
# An nbgitpuller link can also be generated for a binder. Here is a link that will open this notebook in mybinder.org.
# 
# ```
# https://mybinder.org/v2/gh/pangeo-data/pangeo-docker-images/2021.09.30?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fearth-env-data-science%252Fearth-env-data-science-book%26urlpath%3Dtree%252Fearth-env-data-science-book%252Fearth-env-data-science-book%252Fsrc%252Flectures%252Fenvironment%252Fbinder.ipynb%26branch%3Dmaster
# ```
# 
# ```
# https://mybinder.org/v2/gh/pangeo-data/pangeo-docker-images/2021.09.30?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fearth-env-data-science%252Fearth-env-data-science-book%26urlpath%3Dlab%252Ftree%252Fearth-env-data-science-book%252Fsrc%252Flectures%252Fenvironment%252Fbinder.ipynb%26branch%3Dmaster
# ```
# 
# Yes, very complicated and messy. But it works! As with a regular binder, you can hide it behind a button link.

# ### Pangeo Docker Images
# 
# For students of this class, when creating your first binder, we recommend _not defining your own environment from scratch_ but rather using the default environment that comes with our JupyterHub.
# This environment is curated and automatically built into a Docker containter at https://github.com/pangeo-data/pangeo-docker-images.
# The list of official "tags" is at https://github.com/pangeo-data/pangeo-docker-images/tags -- you can see that a new image is released every few weeks.
# The built Docker images live at https://hub.docker.com/r/pangeo/pangeo-notebook/tags.
# 
# Our class has been using the tag `2021.09.30`.
# 
# To create a binder that uses this environment
# - Go to https://jupyterhub.github.io/nbgitpuller/link.html
# - Click the "binder" tab
# - In "Git Environment Repository URL" specify `https://github.com/pangeo-data/pangeo-docker-images`
# - In "Branch" specify `2021.09.30`
# - In "Git Content Repository URL" put the _GitHub link to YOUR repo_.
# 

# ## Creating your Own Binder
# 
# When creating your own binder, you have two options:
# - Use a pre-existing environment
# - Define your own custom environment.
# 
# ### Using a pre-existing environment
# 
# In this case, all you need is a GitHub repo with one or more notebooks in it.
# Then use the nbgitpuller approach described above.
# 
# ### Defining a custom environment
# 
# To create your own binder with a custom environment, you will need two ingredients:
# 
# - Some code to share
# - An appropriate environment
# 
# First create new github repo with the following file / directory structure:
# 
#     binder/environment.yml
#     some-notebook.ipynb
#     Readme.md
# 
# Fill out your environment.yml with your desired packages.
# (See the [lesson on python environments]({filename}/Lectures/python_environments.md) to review how to specify environments.)
# 
# Then add some basic content to the notebook. For example, try importing the packages you might want to use:
# 
#     import numpy as np
#     import pandas as pd
#     import xarray as xr
#     import cartopy.crs as ccrs
#     from matplotlib import pyplot as plt
#     
# Once things are working, push the repo to github. Then use <https://mybinder.org> to generate a binder badge and add it to your `Readme.md` file.
# 
# You should now be able to run your binder on mybinder.org!

# ### Updating your Binder
# 
# An important thing to remember is that **you cannot save changes from within a running binder**. The running notebooks will automatically shut down after 10 minutes of inactivity, and you will **lose any modifications you made to the notebooks**. (See [mybinder FAQ](https://mybinder.readthedocs.io/en/latest/faq.html) for more details.) This is very different from our research computing jupyterhub, where all changes are saved. Binder is meant for demonstrating and sharing finished projects, not development of new ones.
# 
# To update your binder, you need to go back to your personal copy of the repo, make changes, commit, and push back to github.

# In[ ]:




