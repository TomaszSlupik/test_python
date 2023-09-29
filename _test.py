import pytest
import math
import pandas as pd 

x = 'Tomek'

# 1 - dodawanie
def test_sum():
    assert 1 + 1 == 2

# 2 - stringi
def test_string():
    assert isinstance(x, str)

# 3 - sprawdzenie float - dodawanie 
def test_floatNumber ():
    resultFloat = 0.2 + 0.5
    assert math.isclose(resultFloat, 0.7, rel_tol=1e-9)


# 4 
def test_Equal ():
    v1 = 2
    v2 = 2
    assert v1 == v2, f"Liczba {v1} nie jest równa {v2}"

# 5 int
def test_Int():
    v1 = 90
    assert isinstance(v1, int), f"Liczba {v1} nie jest typu intiger"

# 6 DataFrame
def test_DataFrame():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert isinstance(df, pd.DataFrame)

# 7