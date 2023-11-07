import pytest
from is_mutant import is_mutant

@pytest.mark.parametrize("a, res", [
    (["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"], True),
    (["ATGCGA","CAGTGC","TTGTAT","AGAAGG","CCCCTA","TCACTG"], False),
    (["AAGTCA","TTGCAT","GCAGTG","TGATGC","AGTCAG","ATAGTA"], True),
    (["AAGTCA","TTGCAT","GCAGTG","TGATCC","AGCCAG","AGTCAG"], False),
    (["ACTACG","CGTATG","TCTGCA","AGCCGT","TGCCAT","ACCTGG"], True),
    (["ACTACG","CGTATG","TCTGTA","AGCTGT","TGACCT","CCCTGG"], False)
])
def test_is_mutant(a, res):
    assert is_mutant(a) == res
