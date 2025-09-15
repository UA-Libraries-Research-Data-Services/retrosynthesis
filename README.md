# Retrosynthesis Workshop Materials

## About

> [!NOTE]
> 
> Oct 21, 2024 - This repository has recently been transferred from The University of Alabama Libraries Web Services GitHub to The University of Alabama Libraries Research Data Services GitHub organization.
> All GitHub related hyperlinks should automatically redirect to the new GitHub location, but if you notice anything that is not working correctly, please let us know.

**V.F. Scalfani, The University of Alabama**

Workshop materials for teaching computer-assisted retrosynthesis at The University of Alabama Libraries. This workshop code is licensed under the MIT License (the LillyMol workshop content is Apache License 2.0). However, these scripts may depend on external software and libraries, which must be installed separately and are subject to their own licenses. Please refer to their respective documentation for installation instructions and licensing details.

Fall 2024

## How to Run the Notebooks

All code was developed and tested locally on Linux Ubuntu 22.04 LTS. Development environments were set up manually with conda-forge Miniforge (See notebooks). The code was originally developed and tested during September 2024, however, when updates were made in July/September 2025, a new local conda-forge environment was setup (as shown in notebook tutorials) and only updated notebooks were tested. We did not use the original exported conda-forge environment settings when updates were made, so these files are no longer accurate and have been removed.

The tutorials will **not** generally work on Windows as the multiprocessing code would be different on Windows. The code is **not** fully tested on Mac OS (e.g., we have only compiled LillyMol on Linux). In 2024, we had a setup script useful for running the notebooks on GitHub Codespaces, but this no longer fully works and so has been removed. In summary, we recommend running the notebooks locally using Linux or Windows Subsystem for Linux. In future workshops at The University of Alabama, we will explore and test options for cloud/server computing setup.

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


