#Very basics of tests

import pytest
import time

import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_zero():
    #Używa konstrukcji pytest.raises(ZeroDivisionError) w bloku with, aby upewnić się, że ten konkretny wyjątek zostanie wywołany. Jeśli tak się stanie, test przechodzi pomyślnie. W przeciwnym razie test zakończy się niepowodzeniem.
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0)

def test_add_strings():
    result = my_functions.add("I like ", "burgers")

    assert result == 'I like burgers'

#pytest -m slow - puszcze wszystkie testy z tym zaznaczeniem
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


#Pomija test, jest rowniez skipif
@pytest.mark.skip(reason="This feature is broken")
def test_add():
    assert my_functions.add(number_one=1, number_two=4) == 6


@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_zero_broken():
        my_functions.divide(10, 0)