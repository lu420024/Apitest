import pytest

from utils.read_data import get_data
from utils.yaml_util import func_yaml


@pytest.mark.parametrize("data", get_data["person"])
def test_person(data):
    print(func_yaml(data))

