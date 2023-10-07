# Resources
This is a set of libraries for developing data applications with Python. Please text Jeff or drop a message in the Discord server if you need any help.

## Installing Miniconda or Micromamba
If you're exploring the datasets provided by Barrios or playing around with prototypes, you may not want to use the big, heavy DevContainer Jeff provided. In that case, you may want to use a more lightweight solution to setting up local development environments. Miniconda/Micromamba are the tools to use for that.

Miniconda is a smaller version of Anaconda.
[Installing Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)

Micromamba is a parallelized version of Miniconda. It woeks in exactly the same way, but it's supposedly faster(?).
[Installing Micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html)

If you don't want to mess around with virtualized environments on your own, we suggest you just use the DevContainer.

## Pandas
Pandas is a data analysis and manipulation library for Python. If you're working with tabular data, knowing how to use this library is important. Luckily, the Pandas maintainers have written an excellent series of tutorials to help get you up to speed.

[Pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)

## Numpy
Numpy is another Python tool for working with data. There may be times when you need to use Numpy to manipulate multidimensional arrays (Numpy's primary data structure). This is the library to use when you have an array of values that you want to perform mathematical operations on.

[NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)

## Data Exploration and Analysis
[An Extensive Step by Step Guide to Exploratory Data Analysis](https://towardsdatascience.com/an-extensive-guide-to-exploratory-data-analysis-ddd99a03199e)

## Machine Learning
There may be a few ways to approach this project. After looking at the provided data and doing some research, machine learning seems to be a viable solution. Specifically, supervised machine learning that uses regression modeling. See the below introduction by Google.
- [Google - Intro to Machine Learning](https://developers.google.com/machine-learning/intro-to-ml)
- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) - be sure to look at the prerequisites (NumPy, Pandas, etc., which we'll most likely need to use regardless of our approach)

If we decide to use ML, we should stick to some guidelines to make sure the project stays on track:
- [Google - Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml#rule_1_dont_be_afraid_to_launch_a_product_without_machine_learning)

Machine Learning offers some approaches and frameworks, but it will require a fair bit of study and experimentation to choose the correct method. It's worth mentioning that FB Prophet, which was Jeff's initial suggestion, was not a favorite among practitioners in the discussion thread.
- [A discussion of different ML time-series frameworks](https://www.reddit.com/r/MachineLearning/comments/114d166/discussion_time_series_methods_comparisons/)

- [M5 Forecasting Competition](https://www.innovating-automation.blog/m5-forecasting-competition/)

A couple of frameworks that were mentioned in the above discussion. We don't necessarily have to use these and, in fact, it might be a mistake to leap into one of these without a fundamental understanding of ML basics.

- [Nixtla mlforecast](https://github.com/Nixtla/mlforecast)
- [Darts](https://unit8co.github.io/darts/index.html)

## Project Organization
Tools andd techniques for keeping a complex team project organized.

### Monorepos (?)
> [!IMPORTANT]
> This is just an idea. But it seems like it could be a good way to organize the project.

A monorepo is a Git repository that is split into individual packages. Each package in the monorepo represents an individual sub-project and packages can be interdependent. Each package also defines its own dependencies and can have its own virtual environment. This means one team member can work on `barrios/forecasting` while another works on `barrios/server` with less chance of getting in each other's way.

It also means that code from one project can import code from another project. For example, a `ForecastService` class in `barrios/server` might import the `Forecaster` class from `barrios/forecasting`.

Here's what that might look like for a project like ours:

```bash
/barrios
  |- /data                # package 1
      |- pyproject.toml
      |- csv/ # the data
  |- /analysis            # package 2
      |- requirements.txt
      |- pyproject.toml
      |- Analyzer.py
  |- /forecasting         # package 3
      |- requirements.txt
      |- pyproject.toml
      |- Forecaster.py
  |- /optimization        # package 4
      |- requirements.txt
      |- pyproject.toml
      |- Optimizer.py
  |- /server              # package 5
      |- requirements.txt
      |- pyproject.toml
      |- server.py
      |- /...etc
  |- /client              # package 6
      |- package.json
      |- /src
```
