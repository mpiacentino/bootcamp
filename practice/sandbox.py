def check_is_valid(seq):
    """Check sequence for validity, i.e. only nucleotides."""
    for base in seq:
        if base not in bootcamp_utils.bases:
            raise RuntimeError(base + ' is not a valid nucleotide.')
            
def check_seq_longer_than_block(seq, block_size):
    """Confirm that requested block size is smaller than the input sequence."""
    if block_size > len(seq):
        raise RuntimeError('Block size is longer than sequence input.')
        
def prep_seq(seq):
    """Convert sequence to uppercase"""
    return seq.upper()

def blocks(seq, block_size):
    """Divide sequence into blocks and calculate GC content per block."""
    
    check_is_valid(seq)
    check_seq_longer_than_block(seq, block_size)
    
    blocks = ()
    j = block_size

    for i in range(0, len(seq), j):
        block = seq[i:i+j]
        if len(block) < j:
            pass
        else:
            blocks = blocks + (block,)


def gc_blocks(seq, block_size):
    """Divide sequence into blocks and calculate GC content per block."""
    
    gc_cont = ()
    blocks = blocks(seq, block_size)
    
    for i in range(len(blocks)):
        block = blocks[i]
        gc_cont = gc_cont + (((block.count('C') + block.count('G')) / block_size),)
    

#def gc_map(seq, block_size, gc_thresh):
    