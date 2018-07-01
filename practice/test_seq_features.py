import pytest
import seq_features as sf

#Assert will perform the test and do nothing if it works, otherwise it will return an ugly error
def test_number_negatives_single_aa():
    """test if function calls negatives correctly from a single AA input"""
    assert sf.number_negatives('E') == 1
    assert sf.number_negatives('D') == 1
    assert sf.number_negatives('R') == 0
    assert sf.number_negatives('K') == 0
    assert sf.number_negatives('H') == 0


def test_number_negatives_short_seqs():
    """test if function calls negatives correctly from a short AA sequence input"""
    assert sf.number_negatives('EEEEEAAAA') == 5

def test_number_negatives_lowercase():
    """test if cases are lower"""
    assert sf.number_negatives('adseds') == 3
    
def test_number_negatives_invalid_amino_acid():
    """what if we have a non-amino acid input"""
    with pytest.raises(RuntimeError) as excinfo:    #this will help make sure we raise an error
        sf.number_negatives('Z')                    #here we're saying "what happens if we hit this error because of this input"
    excinfo.match('Z is not a valid amino acid')    #this should be the response, so it's testing the test
     
def test_number_positives_single_aa():
    """test if function calls positives correctly from a single AA input"""
    assert sf.number_positives('E') == 0
    assert sf.number_positives('D') == 0
    assert sf.number_positives('R') == 1
    assert sf.number_positives('K') == 1
    assert sf.number_positives('H') == 1

def test_number_positives_short_seqs():
    """test if function calls positives correctly from a short AA sequence input"""
    assert sf.number_positives('EEEEEAAAA') == 0
    assert sf.number_positives('KRAKRHAAAAA') == 5

def test_number_positives_lowercase():
    """test if cases are lower"""
    assert sf.number_positives('adseds') == 0
    
def test_number_positives_invalid_amino_acid():
    """what if we have a non-amino acid input"""
    with pytest.raises(RuntimeError) as excinfo:    #this will help make sure we raise an error
        sf.number_positives('Z')                    #here we're saying "what happens if we hit this error because of this input"
    excinfo.match('Z is not a valid amino acid')    #this should be the response, so it's testing the test

def test_is_valid_with_Z():
    """Perform unit tests on for invalid sequence"""""
    with pytest.raises(RuntimeError) as excinfo:
        sf.is_valid('Z')
    excinfo.match('Z is not a valid amino acid')
    
