import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('input, result', [("katya","Katya")])
def test_capitilize_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(input)
    assert res == result