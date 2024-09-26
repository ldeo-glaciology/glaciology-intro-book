# The Glaciology Data Analysis and Modeling book

## Introduction
This book is a collaborative effort across the international glaciology community to document key glaciological concepts and computational approaches for observing and understanding them. We aim to do this in an **open** and **understandable** way.

By **open** we mean that this is a free resource for everyone and anyone can contribute (see the [Contributing](sec:contributing) section below). This also means that all data used in examples are openly accessible online, often in cloud-optimized, analysis ready formats. It also means that it uses an open-source code base: the Python scientific computing ecosystem.

By **understandable** we mean that we will aim to explain all concepts and computational procedures in sufficient detail such that those who are just starting their career in glaciology will be able to fully comprehend them. In other words, we endeavor to assume very little prior knowledge about glaciological, computational or advanced mathematical concepts.

## Who is this book for?
- undergraduate or early graduate students of glaciology looking to learn some key concepts and computational approaches
- teachers, professors or lecturers designing glaciological course material
- glaciologists looking for inspiration on how to access datasets in the cloud using Python.

## This book compared to previous texts
Several seminal glaciological textbooks, e.g., Cuffey and Paterson's Physics of Glaciers, have be instrumental in the training of generations of glaciologists. This book cannot hope to be as comprehensive as many such texts, but it does aim to cover similar material. So, despite this overlap, we hope it compliment existing text in several ways:  
1. It will be available to anyone, anytime, at no cost. This removes any barriers to entry usually associated with the cost of textbooks.
2. It will be community driven, with multiple contributors sharing their time and expertise. This will more evenly distribute both the work load and the credit for creating a useful text, and it will enable a larger diversity of topics to be covered than a standard introductory text.
3. It will be easily updatable as the science develops.
4. It will include executable code examples embedded in the text (see below).
5. Key physics concepts (the stress equations, mass conservations) will be explained from close-to first principles.


## Running the code interactively
A great advantage of writing this online textbook as a JupyterBook is that coding examples that accompany the text in order to aid in comprehension can be embedded in-line as code blocks. Even better, the reader can interactively run the code, allowing you to experiment with and gain intuition for the modeling or data-analysis procedure being described.

You can run the code in at least three ways.

### 1. In a temporary environment on this page
We'll start with the most straight forward way for readers to run the code. Using a project called **[hebe]( https://thebe.readthedocs.io/en/latest/index.html)**. On any page that includes a code block (such as this one), hover over the rocket icon in the top right of the screen and click on the **Live Code** menu item that appears. Buttons labelled **Run** and **Restart** appear in each code cell and after a short delay during which the computing resources are spun up, these buttons can be used to run each cell in turn. Note that the code can be edited, allowing you to experiment with it.

Advantages of running the code in this way are that it is right here in the same window as the rest of the text, so you will be able to easily navigate between pages. A disadvantage is that you have little flexibility in how you use the computing environment (you cannot open a terminal, install new packages, or download the results of computations or figures). Another disadvantage is that any edits you make to the code are lost when you close the window and the computing environment shuts down.  


### 2. In a temporary environment in a separate window  
A second option is to start a computing environment in a separate JupyterLab window using Binder. On any page that includes a code block, hover over the rocket icon in the top right of the screen and click on **Binder** menu item that appears. This will start a JupyterLab window running inside a Binder session on computing resources supplied MyBinder.org which will enable you to navigate to, edit and run all the notebooks in this book. The advantage of using this approach is that you have the flexibility of the JupyterLab environment, meaning that results of computation or figures can be downloaded, new packages can be installed etc. This approach shares one disadvantage with the first option above, in that when you close the JupyterLab/Binder session you lose all changes and results.

### 3. On your local machine
A third option is to download and run the notebooks on your local machine. The advantage of this approach is that you will have full flexibility on how you run the code and you can make edits which can be saved locally.

The easiest way to download the notebooks is to clone the GitHub repo where this book lives as follows. In the terminal run
```
git clone https://github.com/ldeo-glaciology/glaciology-intro-book.git
```
  `````{note}
  If this does not work try

  ```
  git clone git@github.com:ldeo-glaciology/glaciology-intro-book.git
  ```
  depending on how you have git permissions setup on your machine, it may be necessary to use this version
  `````

Next you will need to install the python packages needed to run the notebooks in this JupyterBook. The easiest way to do this is using [Conda](https://docs.conda.io/en/latest/). Follow the instructions on the Conda website to install Conda, then in the terminal run
```
conda env create -f path/to/cloned/repo/glaciology-intro-book/environment.yml
```

Finally, run
```
jupyter-lab
```
in the terminal and a JupyterLab session will start up. You are now ready to start running the notebooks on your local machine.

(sec:contributing)=
## Contributing
The best way to contribute to this book is to engage through the Github repository that stores the book. This can be found [here](https://github.com/ldeo-glaciology/glaciology-intro-book).

Any suggestions for additional content, corrections, or thoughts are very welcome in the form a GitHub issue. Please do not hesitate to create a new [issue](https://github.com/ldeo-glaciology/glaciology-intro-book/issues).

Pull requests with correction, additional material, or entire new pages or chapters are also very welcome. But the first stop if you want to contribute something should probably be creating a new issue, so that everyone knows what everyone else is interested in working on.

## License

The book is licensed under the [MIT License](https://github.com/ldeo-glaciology/glaciology-intro-book/blob/main/LICENSE.MD).

[![image](https://github.com/user-attachments/assets/e0ec131e-4f81-4d20-8a93-ef04adb57396)](https://github.com/ldeo-glaciology/glaciology-intro-book/blob/main/LICENSE.MD)