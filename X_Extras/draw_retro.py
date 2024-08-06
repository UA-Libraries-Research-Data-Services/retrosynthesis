#!/usr/bin/env python
# coding: utf-8

# Adapted from https://github.com/vfscalfani/rdkit_bookmarks/blob/main/01_retrosynthesis_arrow/arrow.ipynb

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdChemReactions
from rdkit.Chem.Draw import rdMolDraw2D
import re

# Draw rxn and save SVG as a list (each line is a list element)
def create_rxn_svg(rxn, width, height, BondIdxs=False):
    drawer = rdMolDraw2D.MolDraw2DSVG(width,height)
    drawer.drawOptions().fixedScale = 0.4
    drawer.drawOptions().addBondIndices = BondIdxs
    drawer.DrawReaction(rxn)
    drawer.FinishDrawing()
    rxn_svg = drawer.GetDrawingText()

    # create a list of strings
    rxn_svg_split = rxn_svg.split("\n")

    # add a newline character at end of each element
    svg_list = []
    for svg_string in rxn_svg_split:
        svg_list.append(svg_string + '\n')
    # remove extra newline at end
    svg_list.pop()
    return svg_list

def add_retro_arrow(svg_list):

    ### 1. Add a second horizontal line
    # loop through list in reverse and
    # locate the 3rd occurence of <path d='M...
    # this is the arrow line

    svg_retro = []
    for idx, svg_line in enumerate(reversed(svg_list)):
        if svg_line.startswith("<path d='M"):
            # locate 3rd occurence
            if idx == 3:
                # add a copy of this line before (in reverse)
                svg_retro = svg_list.copy()
                svg_retro.insert(-3, svg_line)

    # shift the newly added line in Y vertical position
    # find float numbers with regex, first 4 numbers is all we need.

    l1 = re.findall(r'\d+\.\d+', svg_retro[-4])
    l1_nums = [float(num) for num in l1]
    l1_X1, l1_Y1, l1_X2, l1_Y2 = l1_nums[:4]

    # format new string, shift vertical by 5 units
    
    end_string = "' style='fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:2.0px;stroke-linecap:" + \
    "butt;stroke-linejoin:miter;stroke-opacity:1' />\n"

    svg_retro[-4] = "<path d='M " + str(l1_X1) + "," + str(l1_Y1 + 5) + " L " + \
        str(l1_X2) + "," + str(l1_Y2 + 5) + end_string

    ### 2. Increase size of arrowheads and shift arrowhead vertically between lines
 
    # get positions for arrowheads, which are lines idx -3,-2
    a1 = re.findall(r'\d+\.\d+', svg_retro[-3])
    a2 = re.findall(r'\d+\.\d+', svg_retro[-2])

    a1_nums= [float(num) for num in a1]
    a2_nums= [float(num) for num in a2]

    a1_X1, a1_Y1, a1_X2, a1_Y2 = a1_nums[:4]
    a2_X1, a2_Y1, a2_X2, a2_Y2 = a2_nums[:4]

    # Compute new longer draw position for arrow head (3x original length):

    a1_X2_new = round((a1_X1 + 3 * (a1_X2 - a1_X1)),1)
    a1_Y2_new = round((a1_Y1 + 3 * (a1_Y2 - a1_Y1)),1)
    a2_X2_new = round((a2_X1 + 3 * (a2_X2 - a2_X1)),1)
    a2_Y2_new = round((a2_Y1 + 3 * (a2_Y2 - a2_Y1)),1)

    # format new strings with longer arrowheads
    # also included is to shift the Y positions down between the lines (half the distance from step 1)
    
    svg_retro[-3] = "<path d='M " + str(a1_X1) + "," + str(a1_Y1 + 2.5) + " L " + \
        str(a1_X2_new) + "," + str(a1_Y2_new + 2.5) + end_string

    svg_retro[-2] = "<path d='M " + str(a2_X1) + "," + str(a2_Y1 + 2.5) + " L " + \
        str(a2_X2_new) + "," + str(a2_Y2_new + 2.5) + end_string

    ### 3. Finally, shorten arrow lines a little, so they don't overlap with arrowhead
    # this just adjusts the X2 value

    svg_retro[-4] = "<path d='M " + str(l1_X1) + "," + str(l1_Y1 + 5) + " L " + \
          str(l1_X2 - 5) + "," + str(l1_Y2 + 5) + end_string

    l2 = re.findall(r'\d+\.\d+', svg_retro[-5])
    l2_nums = [float(num) for num in l2]
    l2_X1, l2_Y1, l2_X2, l2_Y2 = l2_nums[:4]

    svg_retro[-5] = "<path d='M " + str(l2_X1) + "," + str(l2_Y1) + " L " + str(l2_X2 - 5) + \
          "," + str(l2_Y2) + end_string
   
    retro_rxn_svg = ''.join(svg_retro)
    return retro_rxn_svg
