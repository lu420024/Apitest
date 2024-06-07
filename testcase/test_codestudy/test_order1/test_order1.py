import pytest


@pytest.mark.run(order=2)
def test_order1():
    print("order1...")