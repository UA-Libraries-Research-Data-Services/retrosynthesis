#!/bin/bash

# September 2025 - changed rdcanon install to use pip

# Update and install dependencies
echo $"Updating and installing dependencies\n"
echo $"\n\n\n"
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    zlib1g-dev \
    libre2-dev \
    cmake \
    libeigen3-dev \
    wget \
    jq \
    unzip

# Unzip the datasets used in the tutorials
echo $"Unzipping retrosynthesis data\n"
echo $"\n\n\n"
unzip X_Data/rxns_100k.zip -d X_Data/
unzip X_Data/Thesis_compounds_ESI.zip -d X_Data/
unzip X_Data/Schneider_JCIM_2016_56_2336_dataSetB.zip -d X_Data/

# Create the 'retro_rdkit_env' environment and install packages
echo $"Creating the 'retro_rdkit_env' environment and installing packages\n"
echo $"\n\n\n"
conda create --name retro_rdkit_env -y
conda run -n retro_rdkit_env conda install -c conda-forge rdkit jupyterlab numpy matplotlib pandas -y

# Create the 'retro_aizynth_env' environment and install packages
echo $"Creating the 'retro_aizynth_env' environment and installing packages\n"
echo $"\n\n\n"
conda create --name retro_aizynth_env -y
conda run -n retro_aizynth_env conda install -c conda-forge "python>=3.9,<3.11" "numpy<2.0" pip -y
conda run -n retro_aizynth_env pip install aizynthfinder[all]
echo $"Downloading public data for AizynthFinder\n"
cd 04_AiZynthFinder
mkdir -p aizynth_data
conda run -n retro_aizynth_env download_public_data aizynth_data
cd ..

# Create the 'retro-sim-env' environment and install packages
echo $"Creating the 'retro-sim-env' environment and installing packages\n"
echo $"\n\n\n"
conda create --name retro-sim-env -y
conda run -n retro-sim-env conda install -c conda-forge rdkit pip -y
conda run -n retro-sim-env pip install rdchiral rdcanon
cd ..

# Clone and build the LillyMol project
echo $"Cloning and building the LillyMol cmake project\n"
echo $"\n\n\n"
git clone https://github.com/vfscalfani/LillyMol_6_cmake.git
cd LillyMol_6_cmake/src
mkdir build
cd build
cmake ..
make -j 4
