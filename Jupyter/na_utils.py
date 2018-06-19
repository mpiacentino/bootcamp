#if you want to write something custom that you'll want to import over and over again, might as well write your own module!
#write in text editor and have a filename that ends in .py

"""
Utilities for parsing nucleic acid sequences.
"""

def rna(seq):
    """
    Convert a DNA sequence to RNA.
    """

    # Determine if original sequence was uppercase
    seq_upper = seq.isupper()

    # Convert to lowercase
    seq = seq.lower()

    # Swap out 't' for 'u'
    seq = seq.replace('t', 'u')

    # Return upper or lower case RNA sequence
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """
    Convert a DNA sequence into its reverse complement as RNA.
    """

    # Determine if original was uppercase
    seq_upper = seq.isupper()

    # Reverse sequence
    seq = seq[::-1]

    # Convert to upper
    seq = seq.upper()

    # Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return result
    if seq_upper:
        return seq.upper()
    else:
        return seq