#!/usr/bin/env python
"""Provides statistical tests and distributions.

Also provides NumberList and FrequencyDistribution, two classes for
working with statistical data.
"""
__all__ = ['distribution', 'histogram', 'kendall', 'ks', 'special', 'test',
           'util']

# GAH: this is a temporary introduction, so users get notice of structure change and
# renaming of this function
from distribution import chi_high as chisqprob

__author__ = ""
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Gavin Huttley", "Rob Knight", "Sandra Smit",
                    "Catherine Lozupone", "Micah Hamady"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"