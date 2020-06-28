# willa-thesis
### Basic data scraping and analysis of 2000+ documents

This repo contains the document analysis for my sister's Master's Thesis.  To run, you will need up to date Python and a few packages.  To get started, download the current [Anaconda package manager for your OS using this link](https://www.anaconda.com/products/individual).  Once downloaded, install.

Once installed, open the Anacona Package Manager and make sure that Jupyter Notebook is installed, if not, install it.

After, you will need to install all other necessary components via your command-line-tool, on Mac it is called Terminal.  For each of the below sections, copy and paste each line individually into Terminal and hit Enter.

### Steps

Create a new conda environment
```
conda create -n willa_thesis
```
Activate
```
conda activate willa_thesis
```
Install the [pandas](https://pandas.pydata.org) data analysis library for Python
```
conda install pandas
```
install [pip](https://pip.pypa.io/en/stable/installing/) (Package Installer for Python)if you do not have it
```
pip install -U pip
```
Install the [textract](https://textract.readthedocs.io/en/stable/python_package.html) lib to read the pdf's
```
pip install textract
```

Once you have done everything here, open a Jupyter Notebook kernal using the same method, this will open a page in your browser, which is where jupyter notebook lives(generally).
```
jupyter notebook
```
(To quit the jupyter notebook, you can press cntl-c in terminal, or just quit Terminal.)

Navigate the willa_thesis folder on your computer, go into the **src** folder, and select the ***willa_thesis.ipynb***.  This will open the notebook and you will be able to follow the individual cells to create the csv's.  You will need to download the articles from this [Google Drive link](https://drive.google.com/drive/folders/1KjyGS0AHJXfPvSBV3otSu9rGKxEbfAGX?usp=sharing).

In the notebook, you will need to specify the folderpath of this directory, wherever you decide to keep.  To get the path on Mac, you can right-click the folder icon, press alt-option, and then select the 'Copy Filepath Name option'.

Or, you can just view the completed csv's in the **finished_csvs** directory/folder.

