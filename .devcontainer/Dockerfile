# Use an official miniconda image as a base
FROM mcr.microsoft.com/vscode/devcontainers/miniconda:latest

# Update and install dependencies for LillyMol
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libre2-dev \
    cmake \
    libeigen3-dev \
    wget \
    unzip

# Unzip the data for the retrosynthesis project
RUN unzip X_Data/Schneider_JCIM_2016_56_2336_dataSetB.zip -d X_Data/

# Create aizynth_data directory and download public data
RUN mkdir aizynth_data && \
    download_public_data aizynth_data

# Create the 'myenv' environment and install packages
RUN conda create --name myenv -y && \
    conda run -n myenv conda install -c conda-forge rdkit jupyterlab numpy matplotlib pandas networkx -y
