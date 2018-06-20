import os

def parseFASTA(in_file, out_file):
    """Take FASTA file and export new file of a str containing full sequence without header"""

    with open(in_file, 'r') as f, open(out_file, 'w') as f_out:
        seq = ''
        next(f)
        for line in f:
            seq += line.rstrip();
        f_out.write(seq)
	#testing comment        
    print(seq[:500] + '...')
