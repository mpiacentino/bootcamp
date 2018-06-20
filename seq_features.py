import bootcamp_utils

def is_valid(seq):
    """Check sequence for validity"""
    for aa in seq:
        if aa not in bootcamp_utils.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

            
def prep_seq(seq):
    """Prepare sequence for counting"""
    return seq.upper()


def number_negatives(seq):
    """Determine number of negatively charged amino acids in a sequence"""
    seq = prep_seq(seq)
    is_valid(seq)
    return seq.count('E') + seq.count('D')


def number_positives(seq):
    """Determine number of positively charged amino acids in a sequence"""
    seq = prep_seq(seq)
    is_valid(seq)
    return seq.count('R') + seq.count('K') + seq.count('H')