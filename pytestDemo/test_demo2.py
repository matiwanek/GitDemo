# file start od ends with test_
#methods with test_
# code in methods
# -k stands for method names execution, -s logs in out put, -v stands for more info metadata
#filename to run specific file
#mark -m (tag) and run tests with the mark (-m name) @pytest.mark.name
#@pytest.mark.skip and @python.mark.xfail (to include test but not post the result)
#fixtures are used as setup and tear methods for test cases - conftest file to generalize
#fixture and make it avaible to all test cases
#datadriven and parametirization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == 'Hi', 'Test failed because strings do not match'

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 ==6, "Addition do not match"

