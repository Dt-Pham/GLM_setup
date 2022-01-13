# GLM_setup
This guide is based on the original [guide](https://github.com/Squeemos/GLM_Processing) from Ben.

## Prerequisite
Have Conda or Miniconda installed.

## Installation

1. Install [Cloud SDK](https://cloud.google.com/sdk/gcloud)

    The data is stored in Google Cloud, therefore we need to install Cloud SDK in order to query those data.
    Follow [this](https://cloud.google.com/sdk/docs/install) to install Cloud SDK.

2. Install [glmtool](https://github.com/deeplycloudy/glmtools)

    The instruction to install glmtool is [here](https://github.com/deeplycloudy/glmtools/blob/master/docs/index.rst).
    
## Get the GLM data

1. Make sure to activate the correct conda environment.

```bash
conda activate glmval
python NCDownloaderInteractive.py
```
