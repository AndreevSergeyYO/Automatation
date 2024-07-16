import pytest
from calculator import Calculator


calculator = Calculator()

@pytest.mark.parametrize( 'nam1, nam2, result', [ (4, 5, 9), (-6, -10, -16), (-6, 6, 0), (5.61, 4.29, 9.9), (10, 0, 10) ] )
def test_sum_positive_nums(nam1, nam2, result):
    calculator = Calculator()
    print("start")
    res = calculator.sum(nam1, nam2)
    assert res == result

@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res  = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)
    

def test_avg_empty_list():
    calculator = Calculator()
    nambers = []
    res  = calculator.avg(nambers)
    assert res == 0

@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()
    nambers = []
    res  = calculator.avg(nambers)
    assert res == 0
    nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res  = calculator.avg(nambers)
    print(res)
    assert res == 5