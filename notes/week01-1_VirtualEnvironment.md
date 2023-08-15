# What is Virtual enviroment?

A virtual environment is a named, isolated, working copy of Python that that maintains its own files, directories, and paths so that you can work with specific versions of libraries or Python itself without affecting other Python projects.

# Why do I care?

* Python is evolving fast.
* Python’s third-party packages are evolving really fast too.
* Different versions are not always compatible.

## Scenario 1

* The versions of Python and packages you used in a project may be out of date after a while.
* If you update the Python and packages, your previous code may not work under new version (Damn!).

## Scenario 2

* Your project A uses Python 2.7 and package a (v1.0)
* Your project B uses Python 3.9 and package a (v2.1)
* You can’t use the default Python on your computer system, as well as other packages, which are set to be a certain version.
  ![image](https://miro.medium.com/max/493/1*YB6YkrefMAj7MRn8nzrvXQ.png)

## Scenario 3

* Your co-worker is working on a project and he is using an Python version that is different from yours.
* He/she sent the project to you ask for collaboration.
* The codes may not work.

## Scenario 4

* Ever wondered why your code works on your laptop fine, but not on your desktop?

## and more ...

# Fix

* To fix this, you can use a **virtual enviroment tool** to produce easily sharable virtual enviroment files.
* Eeach virtual environment can be conceptualized as a separate box where you have the desired Python version and the required packages for your project.
* These boxes are separate such that what you do in one project won’t affect other projects.
* It’s always recommended that you create distinct virtual environments for your projects.

# Setup Virtual Enviroment

Although there are many options to use, **Conda** and **Venv** are enviroment managers that are most popular and widely used. Here, we will use the first option. Setting up virtual enviroment using Venv can be found [here](https://realpython.com/python-virtual-environments-a-primer/).

**Note**: the codes in the following should be typed in:

* Anaconda Prompt (Windows)
* Terminal (Mac)

## Creating virtual environments

First, check out existing virtual environments

```shell
conda env list
```

You should see only one virtual enviroment call *base*, which is created when you install Anaconda.

Now, we show several ways to create a virtual enviroment.

### 1. Building a new virtual environments

```shell
conda create -n my_venv python=3.9.7
```

The above code create an virtual enviroment called *my_venv* with Python version 3.9.7

### 2. Creating a virtual environment by cloning

```shell
conda create -n my_venv_clone --clone my_venv
```

### 3. Creating a virtual environment from a YAML file

```shell
conda env create -n my_venv_3 -f environment.yml
```

## Install specific versions of packages in virtual environments

First, check out existing virtual environments

```shell
conda install matplotlib=3.7.1
```

## Activating virtual environments

After the above creation, we have new virtual environments. Using `shell conda
 env list` you can see the new names. The environment that has asterisk
 indicates the active environment we are in. This means we are still in the base
 environment. To use the newly created virtual environment, we need to activate
 it

```shell
conda activate my_venv
```

Try `shell conda env list` again to see the effect.

## Exporting environment specifications to YAML file

We can check the specifications of the current environment with:

```shell
conda list
```

This will show environment details such as Python version used, package names
installed and their versions. To export the specifications of the current
environment into a YAML file into the current directory, we can use one of the
commands below:

```shell
conda env export -f environment.yml
```

## Deactivating virtual environments

Once you are done using the virtual environment, if you want to switch back to
the base environment, you can use one of the following to deactivate the
environment:

```shell
conda deactivate
```

## Removing virtual environment

After you know you no longer need the virtual environment, you can delete it
using the following code (**make sure to it is deactivated first**):

```shell
conda env remove -n my_venv
```

```shell
conda env remove -n my_venv_clone
```

## Set up for jupyter notebook

1. create a new virtual enviroment

```shell
conda create -n stat2255 python=3.11.4
```

2. activate the virtual environment

```shell
conda activate stat2255
```

3. Install ipykernel and jupyter

```shell
conda install -c anaconda ipykernel
conda install jupyter
```

4. Update to notebook 7

```shell
pip install jupyter notebook --upgrade
```

4. Now you can start notebook 7

```shell
jupyter notebook
```
<!-- 4. Add the stat2255 kernel in jupyter -->

<!-- ```shell -->
<!-- python -m ipykernel install --user --name=stat2255 -->
<!-- ``` -->

<!-- 5. To remove the kernel  -->

<!-- ```shell -->
<!-- jupyter kernelspec uninstall stat2255 -->
<!-- ``` -->

## Reference

[https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28](https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28)

[https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

[https://python.plainenglish.io/virtual-environments-1d09041771d](https://python.plainenglish.io/virtual-environments-1d09041771d)

[https://towardsdatascience.com/beginner-friendly-virtual-environment-management-anaconda-pycharm-36178e20129f](https://towardsdatascience.com/beginner-friendly-virtual-environment-management-anaconda-pycharm-36178e20129f)

```

```
