# Reproducibility Notes

All conda environments are available in this folder for reference. Each tutorial was tested locally on Ubuntu 22.04 LTS with the provided conda environments. The environments were exported as follows:

```
conda env export > environment.yml

```

I would recommend using the latest versions of software first, then if you have issues with software dependencies or notice a change in results behavior, try creating the conda environment from the appropiate yml file in this folder [1]. 

```
conda env create -f environment.yml

```

Note that the LillyMol conda environment was also the `retro_rdkit_env`

[1] https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
