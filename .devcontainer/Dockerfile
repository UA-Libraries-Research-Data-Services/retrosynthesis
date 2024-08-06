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

# Create the 'aizynth1-env' environment and install packages
RUN conda create --name aizynth1-env -y && \
    conda run -n aizynth1-env conda install -c conda-forge "python>=3.8,<3.10" pip=23.0.1 -y && \
    conda run -n aizynth1-env pip install --upgrade pip==23.0.1 && \
    conda run -n aizynth1-env pip install aizynthfinder[all]

# Create the 'retro-sim-env' environment and install packages
RUN conda create --name retro-sim-env -y && \
    conda run -n retro-sim-env conda install -c conda-forge rdkit pip=23.0.1 -y && \
    conda run -n retro-sim-env pip install --upgrade pip==23.0.1 && \
    conda run -n retro-sim-env pip install rdchiral && \
    git clone https://github.com/coleygroup/rdcanon.git && \
    cd rdcanon && conda run -n retro-sim-env pip install -e . && \
    unzip /workspaces/ualibweb/retrosynthesis/X_Data/Schneider_JCIM_2016_56_2336_dataSetB.zip -d /workspaces/ualibweb/retrosynthesis/X_Data/

# Create the 'lillymol-env' environment and install packages
RUN conda create --name lillymol-env -y && \
    conda run -n lillymol-env conda install -c conda-forge rdkit matplotlib jupyterlab -y

# Clone and build the LillyMol project
RUN git clone https://github.com/vfscalfani/LillyMol_6_cmake.git && \
    cd LillyMol_6_cmake/src && mkdir build && cd build && \
    cmake .. && make -j 4

# Create aizynth_data directory and download public data
RUN mkdir /workspaces/ualibweb/retrosynthesis/aizynth_data && \
    download_public_data /workspaces/ualibweb/retrosynthesis/aizynth_data
