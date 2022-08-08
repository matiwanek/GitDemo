import pytest


def test_firstProgram():
    print("Hello")

@pytest.mark.smoke
def test_Greet():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
