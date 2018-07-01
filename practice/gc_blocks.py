import bootcamp_utils

### input checks ###
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




### "meat" of the code here ####

def find_blocks(seq, block_size):
    """Divide sequence into blocks.
    Output is tuple."""
    blocks = ()

    for i in range(0, len(seq), block_size):
        block = seq[i : i + block_size]
        if len(block) < block_size:
            pass
        else:
            blocks = blocks + (block,)
    return blocks

def gc_blocks(seq, block_size):
    """Calculate GC content per block. 
    Output is tuple."""
    gc_cont = ()
    blocks = find_blocks(seq, block_size)
    
    for i in range(len(blocks)):
        block = blocks[i]
        gc_cont = gc_cont + (((block.count('C') + block.count('G')) / block_size),)
    return gc_cont
        

def gc_map(seq, block_size, gc_thresh):
    """Adjust text case based on GC threshold; if above, text is upper, if below, lower.
    Output is a string."""

    blocks = find_blocks(seq, block_size)
    gc_cont = gc_blocks(seq, block_size)
    gc_map_list = []
    
    for i in range(len(gc_cont)):
        if gc_cont[i] >= gc_thresh:
            gc_map_list.append(blocks[i].upper())
        elif gc_cont[i] < gc_thresh:
            gc_map_list.append(blocks[i].lower())

    return ''.join(gc_map_list)
    
    
"""David's approach
        instead of using a tuple for the blocks and gc_cont, he used a list first, populated it, then you can return a tuple
            -however, when i'm building the tuple block by block, it alocates a new tuple in memory each time
            -lists, since mutable, will alocate a larger block of memory, so tuple might be better to do"""