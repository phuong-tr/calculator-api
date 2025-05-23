from app import calc

def test_add():
    assert calc.add(2, 3) == 5

def test_divide_by_zero():
    assert calc.divide(10, 0) == 'Error: Division by zero'
