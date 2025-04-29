import pytest
import guess_number

def test_zgadnij_liczbe():
    assert guess_number.zgadnij_liczbe(50)
    
    python -m pytest test_guess_number.py
