# Retrosynthesis Workshop Materials

## About

> [!NOTE]
> 
> Oct 21, 2024 - This repository has recently been transferred from The University of Alabama Libraries Web Services GitHub to The University of Alabama Libraries Research Data Services GitHub organization.
> All GitHub related hyperlinks should automatically redirect to the new GitHub location, but if you notice anything that is not working correctly, please let us know.

**V.F. Scalfani, The University of Alabama**

Workshop materials for teaching computer-assisted retrosynthesis at The University of Alabama Libraries

Fall 2024

## How to Run the Notebooks

All Jupyter notebooks were developed and tested (during September, 2024) locally on Linux Ubuntu 22.04 LTS. The tutorials will **not** generally work on Windows as the multiprocessing code would be different on Windows. Most of the code *seems* to works on Mac OS; we quickly tested the conda environement setups and ran the notebooks on Mac OS 14.6.1, with an M3 processor. However, we were not able to figure out how to compile LillyMol on Mac OS, so the Lillymol Retrosynthesis notebook will not work without some additional effort. In summary, we recommend running the notebooks locally using Linux or Windows Subsystem for Linux.

Alternatively, if you have a GitHub account, [GitHub Codespaces](https://docs.github.com/en/codespaces), an online computational environment, is another option to run all of the retrosynthesis tutorials. **See the [GitHub Codespaces Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#codespaces) and please note that you may need to adjust your [Codespaces billing](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces) settings and monitor useage to avoid unwanted charges.** There are some free compute hours for each user; more resources are available for a fee. You might also be able to run the notebooks on Google Colab, but you would need to create your own conda and development environments first.

We have included a setup script to help create programming environments for these workshop tutorials in Codespaces. The script installs various software packages using `conda-forge` and `apt-get`, unzips and downloads datasets, and clones two external repositories: one for a Python development installation and another to build its software. Before using the script, we recommend reviewing it, consulting the documentation and licenses of the respective software, and referring to the tutorial notebooks and READMEs in this repository for additional details about the software packages, datasets, and environment setup.

Our initial testing with GitHub Codespaces (VS Code for the Web) suggests that you will need to use at least a 4 core machine for the AiZynthFinder and Similarity-based retrosynthesis workshops. To run the notebooks in Codespaces:

1. On the repository main page, click `code > codespaces > New with options`. Select `Machine type > 4-core > Create codespace`
2. Then, install the needed extensions, including the `Python` and `Jupyter` extensions made by Microsoft.
3. Open a terminal in the codespace, and make the setup script executable: `chmod +x setup.sh`
4. Run the setup script with `./setup.sh`. This will take about 15 minutes and will install system dependencies, download some datasets, create conda environments: `retro_rdkit_env`, `retro_aizynth_env`, and `retro_sim_env`, and download/build the LillyMol C++ software.
5. Verify the conda environments were installed by running `conda info --envs`. Individual packages can be shown with `conda list --name myenv`
6. Verify the LillyMol software works: `cd LillyMol-6-cmake/src/build/build`, then try one of the programs: `./retrosynthesis`. That should bring up a help file.
7. Now, you should be able to run all of the notebooks, be sure to select the appropiate conda environment kernel (see notebook text).
8. Stop the codespace. When finished working, navigate back to the repository main page, and click `code > codespaces (the specific one) > Stop codespace`. You can monitor your useage and billing in your GitHub Settings.

## Planned Workshops

0. [Workshop Series Introduction](https://github.com/ualibweb/retrosynthesis/blob/main/00_Introduction/workshop_intro.ipynb) [*Day 1*]
1. [Python Programming](https://github.com/ualibweb/retrosynthesis/blob/main/01_Python/python_intro.ipynb) [*Day 1*]
2. [RDKit and Cheminformatics Part 1](https://github.com/ualibweb/retrosynthesis/blob/main/02-03_RDKit_Cheminformatics/rdkit_intro_part_one.ipynb) [*Day 2*]
    - SMILES file format
    - Reading and working with molecules
    - Molecule depiction
    - Canonicalization, identifiers, and hashes
    - Chemical similarity and fingerprints
    - Substructure search
3. [RDKit and Cheminformatics Part 2](https://github.com/ualibweb/retrosynthesis/blob/main/02-03_RDKit_Cheminformatics/rdkit_intro_part_two.ipynb) [*Day 3*]
    - Descriptors
    - Reading and working with reactions
    - Reaction depiction
    - Reaction Transformations
    - Molecule and reaction standardization
4. [AiZynthFinder Retrosynthesis](https://github.com/ualibweb/retrosynthesis/blob/main/04_AiZynthFinder/aizynthfinder_rxn_prediction.ipynb) [*Day 4*]
5. [Retorosynthesis based on Similarity Ranking](https://github.com/ualibweb/retrosynthesis/blob/main/05_Similarity_Based/similarity_based_rxn_prediction.ipynb) [*Day 5*]
6. [Lillymol Retrosynthesis](https://github.com/ualibweb/retrosynthesis/blob/main/06_LillyMol/lillymol_rxn_prediction.ipynb) [*Day 6*]

## Notes

> [!CAUTION]
> Retrosynthesis Workshop and Materials Important Considerations

The intention of these retrosynthesis workshops and materials is to provide **introductory, computer-based tutorials** for learning about **published open-source computational cheminformatics techniques** used in retrosynthesis prediction. These tutorials aim to familiarize learners with **algorithm-driven methods for predicting synthetic routes**, using cheminformatics models to explore retrosynthesis. The primary purpose is to enhance learner understanding of cheminformatics strategies for retrosynthetic predictions, not to provide direct, practical laboratory guidance.

**Training Data:** The retrosynthetic prediction techniques in the tutorials use reaction data (and/or computer models derived from this data) from U.S. patents for training purposes. See the [data README](https://github.com/UA-Libraries-Research-Data-Services/retrosynthesis/blob/main/X_Data/AA_README_data) and references in the tutorials for more information.

**Intellectual Property:** Due to the use of patent reaction data, it may be possible that predicted reaction pathways can match or be similar to those reported in patents. Patents are a form of intellectual property, and specific synthetic pathways and compounds may be protected by law [1,2].

**Practical Application:** The techniques taught in these workshop materials are template-based and substructure pattern-driven, meaning they rely on predefined reaction templates and do not capture the full complexity of real-world chemistry. While the cheminformatics techniques taught in these workshop materials can computationally predict synthetic routes, attempting to replicate or use these routes in a laboratory setting would require significant additional research related to synthetic route planning, such as evaluating related reported literature, determining appropriate reaction conditions, considerations of synthesis complexity, and conducting safety assessments. It is important to note that computational models can produce inaccurate or incomplete predictions due to simplifications and assumptions within the algorithms, as well as limitations in their training data, which may not align with real-world chemical behavior. In particular, the computational models do **not account for factors such as reactivity conflicts, potential safety hazards, or incompatibilities between chemical substances. Other limitations may also exist depending on the specific reaction, data, and model used.** Moreover, replication of certain predicted routes may infringe on existing patents. Always verify the suitability and legal status of the methods and compounds before any practical application.

**Alternative Data Sources:** Although patent reaction data is widely used in cheminformatics for reaction prediction due to its availability, it is possible to use non-patent reaction data for these tutorials, such as those extracted from journal articles, to explore synthetic pathways that may not be covered by patents. However, the suitability of any alternative sources should still be assessed.

In summary, please respect intellectual property laws and understand that the provided examples are for educational, computer-based learning purposes. Always consult with your supervisor and legal experts if you plan to apply these techniques in your research, and ensure that thorough safety evaluations are conducted before attempting any laboratory procedures.

[1] What Every Chemist Should Know About Patents (4th), American Chemical Society’s Joint Board-Council Committee on Patents and Related Matters: https://www.acs.org/content/dam/acsorg/about/governance/committees/patents/what-every-chemist-knows-patents.pdf

[2] White, M. J. Chemical Patents. In Chemical Information for Chemists: A Primer; The Royal Society of Chemistry, 2013. https://doi.org/10.1039/9781782620655-00053.


