#!/bin/bash

# Update and install dependencies for LillyMol
echo "Updating and installing dependencies for LillyMol\n"
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    zlib1g-dev \
    libre2-dev \
    cmake \
    libeigen3-dev \
    wget \
    unzip

# Unzip the data for the retrosynthesis project
echo "Unzipping retrosynthesis data\n"
unzip X_Data/Schneider_JCIM_2016_56_2336_dataSetB.zip -d X_Data/

# Create the 'myenv' environment and install packages
echo "Creating the 'myenv' environment and installing packages\n"
conda create --name myenv -y
conda run -n myenv conda install -c conda-forge rdkit jupyterlab numpy matplotlib pandas networkx -y

# Create the 'aizynth1-env' environment and install packages
echo "Creating the 'aizynth1-env' environment and installing packages\n"
conda create --name aizynth1-env -y
conda run -n aizynth1-env conda install -c conda-forge "python>=3.8,<3.10" pip=24.0 -y
conda run -n aizynth1-env pip install aizynthfinder[all]
echo "Downloading public data for AizynthFinder\n"
mkdir -p aizynth_data
conda run -n aizynth1-env download_public_data aizynth_data

# Create the 'retro-sim-env' environment and install packages
echo "Creating the 'retro-sim-env' environment and installing packages\n"
conda create --name retro-sim-env -y
conda run -n retro-sim-env conda install -c conda-forge rdkit -y
conda run -n retro-sim-env pip install rdchiral
git clone https://github.com/coleygroup/rdcanon.git
cd rdcanon
conda run -n retro-sim-env pip install -e .
cd ..

# Create the 'lillymol-env' environment and install packages
echo "Creating the 'lillymol-env' environment and installing packages\n"
conda create --name lillymol-env -y
conda run -n lillymol-env conda install -c conda-forge rdkit matplotlib jupyterlab -y

# Clone and build the LillyMol project
echo "Cloning and building the LillyMol project\n"
git clone https://github.com/vfscalfani/LillyMol_6_cmake.git
cd LillyMol_6_cmake/src
mkdir build
cd build
cmake ..
make -j 4