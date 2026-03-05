from calculator import Calculator

calc = Calculator()

def test_full_operation():
    result = calc.add(5,3)
    assert result == 8

def test_clear():
    result = calc.clear()
    assert result == 0