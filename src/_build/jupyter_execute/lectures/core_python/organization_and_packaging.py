#!/usr/bin/env python
# coding: utf-8

# # Organization and Packaging of Python Projects
# 
# A complex research project often relies and many different programs and software packages to accomplish the research goals. 
# An important part of scientific computing is deciding how to organize and structure the code you use for research.
# A well-structured project can make you a more efficient and effective researcher.
# It is also a key component of [scientific reproducibility](http://lorenabarba.com/blog/barbagroup-reproducibility-syllabus/).
# 
# 
# Just putting all of your code into git repositories won't magically turn a mess of scripts into a beautiful, well-organized project.
# More deliberate effort is required.
# 
# ## Types of Projects
# 
# Not all projects are created equal.
# Based on my experience, I categorize three different types of "research code" scenarios commonly encountered in geosciences.
# 
# 1. **Exploratory analyses**: When exploring a new idea, a single notebook or script is often all we need.
# 1. **A Single Paper**: The "paper" is a standard unit of scientific output. The code related to a single paper usually belongs together. 
# 1. **Reusable software elements**: In the course of our research computing, we often identify specialized routines that we want to package for reuse in other projects, or by other scientists. This is where "scripts" become "software."
# 
# This lecture outlines some suggested practices for each category. 

# ## Exploratory Analysis
# 
# When starting something new, we are often motivated to just start coding and get some results quick.
# This is fine!
# Jupyter notebooks are an ideal format for open-ended exploratory analysis, since they are totally self-contained: they encapsulate text, code, and figures.
# If we find someting cool or useful, it is important to preserve these exploratory notebooks.
# 
# A dedicated github repository can be overkill for a single file.
# Instead, I recommend github's "[gist](https://help.github.com/articles/about-gists/)" mechanism for saving and sharing such "one-off" notebooks and code snippets.
# Gists are like mini repos you can easily share and embed.
# (You can create one right now by going to <https://gist.github.com/>.)
# 
# You can upload any file (including an `.ipynb` notebook file) by dragging and dropping it into the gist website.
# You have the choice of making you gist public or secret. (There is no private option, but a secret gist can only be seen by others if you give them the URL.)
# 
# GitHub's rendering of Gists is a bit buggy. For a more consistent rendering experience, you can share your gist via <http://nbviewer.ipython.org/>.

# ## A Single Paper
# 
# ### Scientific Reproducibility
# 
# Reproducibility is a cornerstone of the scientific process.
# However, today one often reads that science is in the midst of a [reproducibility crisis](http://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970).
# This crisis may be due to increasing complexity and cost of scientific analysis, together with mounting pressure to publish as much and as quickly as possible.
# 
# Today almost all earth science relies on some form of computation, from simple statistical analysis and curve fitting to advanced numerical simulation.
# In principle, computational science should be highly reproducible.
# However, it also brings unique challenges.
# A great overview of the challenges and best practices is given in
# _Barba, Lorena A. (2017): Barba-group Reproducibility Syllabus. figshare. <https://doi.org/10.6084/m9.figshare.4879928.v1>._
# Many of the suggestions in this lecture are adopted or paraphrased from _Barba (2017)_.
# 
# Keep in mind that the audience for a reproducibile project is not just other scientists...it's _you_, a year from now, or whenever you need to repeat and / or build on earlier work. Most scientists build on their Ph.D. work for a decade following graduation. Extra time spent on reproducibility now will make you more productive in the long run.
# 
# We begin with an important observation.
# 
# > An article about computational science … is not the scholarship itself, it’s merely scholarship advertisement. The actual scholarship is the complete software development environment and the complete set of instructions which generated the figures.
# 
# _Donoho, D. et al. (2009), Reproducible research in computational harmonic analysis, Comp. Sci. Eng. 11(1):8–18, doi: [10.1109/MCSE.2009.15](http://dx.doi.org/10.1109/MCSE.2009.15)_
# 
# [Sandve et al. (2013)](http://dx.doi.org/10.1371/journal.pcbi.1003285) give some specific recommmendations for computational reproducibility.
# 
# 1. For every result, keep track of how it was produced
# 1. Avoid manual data-manipulation steps
# 1. Archive the exact versions of all external programs used
# 1. Version-control all custom scripts
# 1. Record all intermediate results, when possible in standard formats
# 1. For analyses that include randomness, note underlying random seeds
# 1. Always store raw data behind plots
# 1. Generate hierarchical analysis output, allowing layers of increasing detail to be inspected
# 1. Connect textual statements to underlying results
# 1. Provide public access to scripts, runs, and results
# 
# These recommendations suggest a certain structure for a project.
# 
# ### Project Layout
# 
# A reproducible single-paper project directory structure might look something like this
# 
#     README.md
#     LICENSE
#     environment.yml
#     data/intermediate_results.csv
#     notebooks/process_raw_data.ipynb
#     notebooks/figure1.ipynb
#     notebooks/figure2.ipynb
#     notebooks/helper.py
#     manuscript/manuscript.tex
# 
# A great example of such a paper is [Cesar Rocha](https://crocha700.github.io/)'s Upper Ocean Seasonality project: <https://github.com/crocha700/UpperOceanSeasonality>.
# 

# ## Reuseable Software Elements
# 
# Scientific software can perhaps be grouped into two categories: single-use "scripts" that are used in a very specific context to do a very specific thing (e.g.~to generate a specific figure for a paper), and reuseable components which encapsulate a more generic workflow. Once you find yourself repeating the same chunks of code in many different scripts or projects, it's time to start composing reusable software elements.

# ### Modules
# 
# The basic element of reusability in python is the [module](https://docs.python.org/3/tutorial/modules.html).
# A module is a `.py` file which contains python objects which can be _imported_ by other scripts or notebooks.
# Let's illustrate how modules work with a simple example.
# 
# A common task in geoscience is to calculate the [great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) between two points on the globe.
# There are several [pacakges](https://pypi.python.org/pypi/geopy) that could do this for you, but let's write our own as an example of a module.
# 
# The formula for great circle distance is
# 
# ![great circle distance formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/75af53b063ee43aed3de186b1a98af5c150185b8)
# 
# (Note that this formula requires 64-bit precision for adequate accuracy.)
# 
# Let's write a module to do this calculation. Open a file called `gcdistance.py` in a text editor. (The file should be in the same directory as the notebook you are working in now.) Populate it with the following code:
# 
# ```python
# """
# A python module for computing great circle distance
# """
# import numpy as np
# 
# # approximate radius of Earth
# R = 6.371e6
# 
# def great_circle_distance(point1, point2):
#     """Calculate great-circle distance between two points.
#     
#     PARAMETERS
#     ----------
#     point1 : tuple
#         A (lat, lon) pair of coordinates in degrees
#     point2 : tuple
#         A (lat, lon) pair of coordinates in degrees
#         
#     RETURNS
#     -------
#     distance : float
#     """
#     
#     # unpack coordinates
#     lat1, lon1 = point1
#     lat2, lon2 = point2
#     
#     # unpack and convert everything to radians
#     phi1, lambda1, phi2, lambda2 = [np.deg2rad(v) for v in 
#                                     (point1 + point2)]
#     
#     # apply formula
#     # https://en.wikipedia.org/wiki/Great-circle_distance
#     return R*np.arccos(
#         np.sin(phi1)*np.sin(phi2) + 
#         np.cos(phi1)*np.cos(phi2)*np.cos(lambda2 - lambda1))
# ```
# 
# The module begins with a [docstring](https://www.python.org/dev/peps/pep-0257/) explaining what it does. Then it contains some data (just a constant `R`) and a single function.
# 
# Now let's import our module

# In[4]:


import gcdistance
help(gcdistance) 


# And let's try using it to make a calculation

# In[2]:


gcdistance.great_circle_distance((60, 0), (50, 15))


# We could just import the function we need

# In[5]:


from gcdistance import R, great_circle_distance
R


# If we change the module, we need to either restart our kernel or else reload the module. (Note that functions imported via `from module import func` cannot be reloaded.)

# In[8]:


from importlib import reload
reload(gcdistance) 


# Modules are a simple way to share code between different scripts or notebooks in the same project. _Module files must reside in the same directory as any script which imports them!_ This is a big limitation; it means you can't share modules between different projects.
# 
# Once you have a piece of code that is general-purpose enough to share between projects, you need to create a package.

# ### Aside: Python Style
# 
# There are few absolute rules for python code style, but there is a detailed [recommended style guide](https://www.python.org/dev/peps/pep-0008/). Some especially relevant points are:
# 
# * Line length should not exceed 79 characters
# * Module names should be `lowercase`
# * Function and variable names should be `lower_case_with_underscores`
# * Class names should be `CamelCase`

# ### Packages
# 
# [Packages](https://docs.python.org/3/tutorial/modules.html#packages) are python's way of encapsulating reusable code elements for sharing with others. Packaging is a huge and complicated topic. We will just scratch the surface.
# 
# We have already interacted with many packages already. Browse some of their github repositories to explore the structure of a large python package:
# 
# * NumPy: <https://github.com/numpy/numpy>
# * Pandas: <https://github.com/pandas-dev/pandas>
# * Xarray: <https://github.com/pydata/xarray>
# 
# An example of a smaller, more understandable package is our group's xrft package:
# 
# * xrft: https://github.com/xgcm/xrft
# 
# These packages all have a common basic structure. Imagine we wanted to turn our great-circle distance module into a package. It would look like this.
# 
#     README.md
#     LICENSE
#     environment.yml
#     requirements.txt
#     setup.py
#     gcdistance/__init__.py
#     gcdistance/gcdistance.py
#     gcdistance/tests/__init__.py
#     gcdistancs/tests/test_gcdistance.py
#     
# The actual package is contained in the `gcdistance` subdirectory. The other files are auxilliary files which help others understand and install your package. Here is an overview of what they do
# 
# | File Name | Purpose |
# |-----------|---------|
# | `README.txt` | Explain what the package is for |
# | `LICENSE` | Defines the legal terms under which other can use the package. [Open source](https://opensource.org/licenses/category) is encouraged! |
# | `environment.yml` | A conda environment which describes the package's dependencies ([more info](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)) |
# | `requirements.txt` | A file which describes the package's dependences for pip. ([more info](https://pip.pypa.io/en/stable/user_guide/#requirements-files))|
# | `setup.py` | A special python script which installs your package. ([more info](https://pythonhosted.org/an_example_pypi_project/setuptools.html)) |
# 

# ### The actual package
# 
# The directory `gcdistance` is the actual package. Any directory that contains an `__init__.py` file is recognized by python as a package. This file can be blank, bu it needs to be present. From the root directory, we can import a module from the package as follows
# 
# ```python
# from gcdistance import gcdistance
# ```
# 
# Yes, this is a bit redundant. That's because the `gcdistance.py` module has the same name as the `gcdistance` package directory.
# 
# However, this import will only work from the parent directory. It is not globally accessible from your python environment.

# `setup.py` is the magic file that makes your package installable and accessible anywhere. Here is an extremely basic `setup.py`
# 
# ```python
# from setuptools import setup
# 
# setup(
#     name = "gcdistance",
#     version = "0.1.0",
#     author = "Ryan Abernathey",
#     packages=['gcdistance'],
#     install_requires=['numpy'],
# )
# ```
# 
# There is a dizzying range of [options](https://setuptools.readthedocs.io/en/latest/setuptools.html) for `setup.py`. More fields are required if you want to [upload your package](https://pythonhosted.org/an_example_pypi_project/setuptools.html) to pypi (so it is installable via `pip`).
# 
# To run the setup script, we call the following from the command line
# 
#     python setup.py install
#     
# The package files are copied to our python library directory.
# If we plan to keep developing the package, we can install it in "developer mode" as
# 
#     python setup.py develop
# 
# In this case, the files are symlinked rather than copied.

# ## Testing
# 
# A software package requires [tests](https://en.wikipedia.org/wiki/Software_testing) to ensure that it works properly. Matt Rocklin has a great [blog post](http://matthewrocklin.com/blog/work/2016/02/08/tests) on why we should write tests for our code.
# 
# Tests don't have to be complicated. They are simply a check to verify that your code does what it is supposed to do.
# 
# To add tests to our project, we create create the file `gcdistance/tests/test_gcdistance.py`. (We also need an `__init__.py` file in the `tests` directory.) The example below shows an example of a test function for our package.
# 
# ```python
# import numpy as np
# import pytest
# 
# from gcdistance.gcdistance import great_circle_distance
# 
# def test_great_circle_distance():
#     # some known results
#     # distance between two same points should be zero
#     assert great_circle_distance((20., 30.), (20., 30.)) == 0
# 
#     # check distance between new york and london
#     new_york = 40.7128, -74.0060
#     london = 51.5074, 0.1278
#     dist_nyc_london = great_circle_distance(new_york, london)
#     
#     # very strict, doesn't actually work
#     # assert dist_nyc_london == 5.587e6
#     
#     # an approximate version of the above
#     np.testing.assert_allclose(dist_nyc_london, 5.587e6, rtol=1e-5)
# 
#     # now check that we can't pass the wrong number of arguments
#     with pytest.raises(TypeError):
#         great_circle_distance(1, 2, 3, 4)
# ```
# 
# We will use [pytest](https://docs.pytest.org/en/latest/getting-started.html) to run our tests. If you don't have pytest installed in your active python environment, take a minute to run `pip install pytest` from the command line. Now run
# 
# ```bash
# py.test -v
# ```
# 
# from the root directory of your project. You should see a notification that the tests passed. Try playing around with the tests to cause something to fail.
# 

# ### Continuous Integration with Travis CI
# 
# You can configure automatic testing of your package by integrating github with [Travis-CI](https://travis-ci.org/). Travis-CI is a free "continuous integration" service: it automatically downloads your package and runs your tests in the cloud every time you commit to your repository. The travis [getting started guide](https://docs.travis-ci.com/user/getting-started) gives a great overview of how to use the service.
# 
# For us to use travis with our project, the steps are simple:
# 
# 1. Push the repo to github (repo must be public)
# 1. Log in to <https://travis-ci.org> and click the switch to enable your repo
# 1. Add a `.travis.yml` file to your project with the following contents:
# 
#         language: python
#         python:
#         - 3.6
#         script:
#         - pytest
# 1. Add the file, commit, and push to github
# 1. Go to <https://travis-ci.org> and watch the magic happen!
# 
