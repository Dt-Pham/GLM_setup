# GLM_setup
This guide is based on the original [guide](https://github.com/Squeemos/GLM_Processing) from Ben.

## Prerequisite
Have Conda or Miniconda installed.

## Installation

1. Install [Cloud SDK](https://cloud.google.com/sdk/gcloud)<br>
    The data is stored in Google Cloud, therefore we need to install Cloud SDK in order to query those data.<br>
    Follow [this](https://cloud.google.com/sdk/docs/install) to install Cloud SDK.

2. Install [glmtools](https://github.com/deeplycloudy/glmtools)<br>
    The instruction to install glmtools is [here](https://github.com/deeplycloudy/glmtools/blob/master/docs/index.rst).
    
3. Install other packages to interact with the data

    ```bash
    conda install -c anaconda netcdf4       # netcdf is the file format of glm data
    conda install jupyter notebook          # to interact .ipynb files
    ```
    
## Download the GLM data

1. Make sure to activate the correct conda environment.

    ```bash
    conda activate glmval
    python NCDownloaderInteractive.py
    ```

## Using the data

[Examples](https://github.com/deeplycloudy/glmtools/tree/master/examples) in the glmtools repository.


## MISC
[Conda Cheatsheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
