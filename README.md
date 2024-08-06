# Retrosynthesis Workshop Materials


V.F. Scalfani, The University of Alabama

[in-progress materials for teaching computer-assisted retrosynthesis at The University of Alabama Libraries]

Fall 2024

> [!NOTE]
> If you find these materials useful for teaching or research, please let me know by either opening an issue or sending me a note: vfscalfani@ua.edu. This helps prioritize my efforts. Contributions and bug reports are appreciated.

**TODO**

* [ ] Create versions of notebooks that run on Google Colab and/or GitHub Codespaces

0. Workshop Series Introduction [*Day 1*]
1. Python Programming [*Day 1*]
2. RDKit and Cheminformatics Part 1 [*Day 2*]
    - SMILES file format
    - Reading and working with molecules
    - Molecule depiction
    - Canonicalization, identifiers, and hashes
    - Chemical similarity and fingerprints
    - Substructure search
3. RDKit and Cheminformatics Part 2 [*Day 3*]
    - Descriptors
    - Reading and working with reactions
    - Reaction depiction
    - Reaction Transformations
    - Molecule and reaction standardization
4. AiZynthFinder Retrosynthesis [*Day 4*]
5. Retorosynthesis based on Similarity Ranking [*Day 5*]
6. Lillymol Retrosynthesis [*Day 6*]

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


## Steps to run in codespaces

1. On the repository 'https://github.com/ualibweb/retrosynthesis', click `code`, then click `codespaces` and `Create codespace on main`
2. Install Extensions: Press `Ctrl+Shift+x` or click the extensions button on the left and install the `Python` and `Jupyter` extensions made by microsoft
3. Create Conda Environment: Press `Ctrl+Shift+P` and type `>Python:Create Environment`. Then click the first option, then `Conda`, then `Python 3.11`
4. Install Basic Packages: Open a new terminal with 'Ctrl+Shift+`' and type 'conda install -c conda-forge rdkit jupyterlab numpy matplotlib pandas networkx'
