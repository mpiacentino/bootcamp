import os

def parseFASTA(input, output):
    """Take FASTA file and export new file of a str containing full sequence without header"""

    with open(input, 'r') as f, open(output, 'w') as f_out:
        seq = ''
        next(f)
        for line in f:
            seq += line.rstrip();
        f_out.write(seq)
	#testing comment        
    print(seq[:500] + '...')
