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

# Create the 'myenv' environment and install packages
RUN conda create --name myenv -y && \
    conda run -n myenv conda install -c conda-forge rdkit jupyterlab numpy matplotlib pandas networkx -y

# Create aizynth_data directory and download public data
RUN mkdir /workspaces/ualibweb/retrosynthesis/aizynth_data && \
    download_public_data /workspaces/ualibweb/retrosynthesis/aizynth_data
