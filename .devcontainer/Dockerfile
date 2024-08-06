# Use an official miniconda image as a base
FROM mcr.microsoft.com/vscode/devcontainers/miniconda:latest

# Update the base Conda environment and pip
RUN conda update -n base -c defaults conda -y && \
    conda install pip=23.0.1 -y && \
    pip install --upgrade pip==23.0.1

# Update and install dependencies for LillyMol
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libre2-dev \
    cmake \
    libeigen3-dev \
    wget \
    unzip

# Set the working directory to the repository root
WORKDIR /workspaces/retrosynthesis

# Unzip the data for the retrosynthesis project
RUN unzip X_Data/Schneider_JCIM_2016_56_2336_dataSetB.zip -d X_Data/

# Create aizynth_data directory and download public data
RUN mkdir aizynth_data && \
    download_public_data aizynth_data
