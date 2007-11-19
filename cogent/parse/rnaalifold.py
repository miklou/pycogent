#!/usr/bin/env python

from string                import strip,split,atof
from cogent.struct.rna2d   import ViennaStructure,Pairs

__author__ = "Shandy Wikman"
__copyright__ = "Copyright 2007, The Cogent Project"
__contributors__ = ["Shandy Wikman"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Shandy Wikman"
__email__ = "ens01svn@cs.umu.se"
__status__ = "Development"

def rnaalifold_parser(lines=None):
    """Parser for rnaalifold stdout output

    Returns a list containing: sequence,structure(pairs object) and energy
    Ex: [seq,[struct],energy]
    """
    result = line_parser(lines)
    return result
    
def line_parser(list=None):
    """Parses RNAalifold output line for line """
    s = False
    seq = ''
    energy = ''
    pairs = ''
    result = []
    for line in list:
        if len(line)>1 and s==False:
            seq = line.strip()
            s = True
        elif s == True:
            s=False
            struct = line.split(None,2)[0].strip('\n')
            energy = atof(line.split(None,2)[1].strip('(\n'))
            pairs = to_pairs(struct)
            pairs.sort()
            
    result.append([seq,pairs,energy])
    return result

def to_pairs(struct=None):
    """
    Converts a vienna structure into a pairs object
    Returns pairs object

    pairs functions tested in test for rna2d.py
    """
    struct = ViennaStructure(struct)
    pairs = struct.toPairs()

    return pairs