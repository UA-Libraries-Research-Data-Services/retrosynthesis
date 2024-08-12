# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Computer Assisted Retrosynthesis'
copyright = '2024, Vincent F. Scalfani'
author = 'Vincent F. Scalfani'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.doctest']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_logo = 'imgs/UALIB_logo.png'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxdoc'
#html_static_path = ['_static']

# hide the sidebar
# See here: https://www.sphinx-doc.org/en/master/usage/theming.html
html_theme_options = {
	"nosidebar": "True"
}
