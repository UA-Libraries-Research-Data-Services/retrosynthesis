# Retrosynthesis Workshop Materials

**TODO**

* [ ] Adjust notebooks so they can run in GitHub Codespaces without needing any changes

         - change config paths to relative and test

         - add instructions for how to git clone lillymol and rdcanon, then install
         
         - add a note that the 0.5 CPU multiplier can be removed

## About

V.F. Scalfani, The University of Alabama

[in-progress materials for teaching computer-assisted retrosynthesis at The University of Alabama Libraries]

Fall 2024

> [!NOTE]
> If you find these materials useful for teaching or research, please let me know by either opening an issue or sending me a note: vfscalfani@ua.edu. This helps prioritize my efforts. Contributions and bug reports are appreciated.

## How to Run the Notebooks

All Jupyter notebooks were developed locally on Linux Ubuntu 22.04 LTS. We think they should also work on Mac OS, but not on Windows as the multiprocessing code would be different on Windows. We recommend running the notebooks locally using Linux or Windows Subsystem for Linux. 

Alternatively, if you have a GitHub account, [GitHub Codespaces](https://docs.github.com/en/codespaces), an online computational environment, is another option to run these retrosynthesis tutorials. Please note that you may need to adjust your [Codespaces billing](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces) settings and monitor useage to avoid unwanted charges. There are some free compute hours for each user; more resources are available for a fee.

Our initial testing on Codespaces suggests that you will need to use at least a 4 core machine for the AiZynthFinder and Similarity-based retrosynthesis workshops. To run the notebooks in Codespaces:

1. On the repository 'https://github.com/ualibweb/retrosynthesis', click `code`, then click `codespaces` and `create codespace on main`
2. Then, install the needed extensions: Press `Ctrl+Shift+x` or click the extensions button on the left and install the `Python` and `Jupyter` extensions made by Microsoft
3. [we are still working on this part] Next, follow the instructions within each notebook to setup the development environment using conda and pip.

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
> Retrosynthesis Workshop and Materials Disclaimer

The intention of these retrosynthesis workshops and materials is to provide introductory computer-based tutorials for learning about published open-source retrosynthetic techniques. These tutorials are designed to enhance end-user chemical information discovery strategies. However, end-users should be aware of the following important considerations:

**Training Data:** The retrosynthetic prediction techniques in the tutorials use publicly available reaction data (and/or computer models derived from this data) from U.S. patents for training purposes.

**Intellectual Property:** Due to the use of patent reaction data, it may be possible that predicted reaction pathways can match or be similar to those reported in patents. Patents are a form of intellectual property, and specific synthetic pathways and compounds may be protected by law [1,2].

**Practical Application:** While the techniques taught in these workshop materials can computationally predict synthetic routes, attempting to replicate or use these routes in a laboratory setting would require additional research such as appropiate reaction conditions and safety considerations. Moreover, replication of certain predicted routes may infringe on existing patents. Always verify the suitability and legal status of the methods and compounds before any practical application.

**Alternative Data Sources:** Although patent reaction data is widely used in cheminformatics for reaction prediction due to its availability, it is possible to use non-patent reaction data for these tutorials such as those extracted from journal articles, to explore synthetic pathways that may not be covered by patents.

In summary, please respect intellectual property laws and understand that the provided examples are for educational computer-based learning purposes. Always consult with legal experts if you plan to apply these techniques in your research.

[1] What Every Chemist Should Know About Patents (4th), American Chemical Society’s Joint Board-Council Committee on Patents and Related Matters: https://www.acs.org/content/dam/acsorg/about/governance/committees/patents/what-every-chemist-knows-patents.pdf

[2] White, M. J. Chemical Patents. In Chemical Information for Chemists: A Primer; The Royal Society of Chemistry, 2013. https://doi.org/10.1039/9781782620655-00053.


