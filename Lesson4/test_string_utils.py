import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize():
    """POSITIVE"""
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello word") == "Hello word"
    assert utils.capitalize("123") == "123"
    """NEGATIVE"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("12345тест") == "12345тест"

def test_trim():
    """POSITIVE"""
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  hello word  ") == "hello word  "
    assert utils.trim("  SKY  ") == "SKY  "
    """NEGATIVE"""
    assert utils.trim("") == ""

"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # """NEGATIVE"""
    ("", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res  = utils.to_list(string, delimeter)
    assert res == result

"""contains"""
@pytest.mark.parametrize('string, symbol, result', [
# POSITIVE
    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
# """NEGATIVE"""
    ("Москва", "м", False),
    ("привет", "з", False),
    ("кот", "№", False),
    ("", "з", False),
    ("12345", "h", False),

])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

"""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [ 
# POSITIVE
    ("корень", "к", "орень"),
    ("Женя", "н", "Жея"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Красная Площадь", " ", "КраснаяПлощадь"),
# """NEGATIVE"""
    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("зелень ", " ", "зелень"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

"""stsrts_with"""

@pytest.mark.parametrize('string, symbol, result', [ 
# POSITIVE
    ("светофор", "с", True),
    ("", "", True),
    ("Москва", "М", True),
    ("Film", "F", True),
    ("Мира-Зина", "М", True),
    ("123", "1", True),
# """NEGATIVE"""
    ("Ваня", "в", False),
    ("мир", "М", False),
    ("", "@", False),
    ("плащь", "ж", False),
    ("зверь", "н", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""

@pytest.mark.parametrize('string, symbol, result', [ 
# POSITIVE
    ("светофор", "р", True),
    ("", "", True),
    ("Москва", "а", True),
    ("Film", "m", True),
    ("Мира-Зина", "а", True),
    ("123", "3", True),
# """NEGATIVE"""
    ("Ваня", "Я", False),
    ("мир", "Р", False),
    ("", "@", False),
    ("плащь", "Ъ", False),
    ("зверь", "m", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""

@pytest.mark.parametrize('string, result', [ 
# POSITIVE
    ("", True),
    (" ", True),
    ("   ", True),
# """NEGATIVE"""
    ("Ваня", False),
    (" мир c пробелом", False),
    ("345", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

"""list_to_string"""

@pytest.mark.parametrize('lst, joiner, result', [ 
# POSITIVE
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
    (["в", "у", "з"], "", "вуз"),
# """NEGATIVE"""
    ([], None, ""),
    ([], ",", ""),
    ([], "кот", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
       res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

