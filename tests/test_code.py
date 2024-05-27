from function import hiding_list
from function import execeted_operation
from function import latest_operation
from function import sorted_date


def test_hiding_list():
    """тестируем скрытие счета
    отображается ли счёт в виде 6 символов и является ли первый символ *"""
    assert len(hiding_list()[0]['to']) == 6
    assert hiding_list()[0]['to'][0] == '*'


def test_execeted_operation():
    """тест первого элемента в списке на принадлежность к успешно выпоненным операциям"""
    assert execeted_operation()[0]["state"] == "EXECUTED"


def test_sorted_date():
    """тест на количество отображаемых элементов в виджете"""
    assert len(sorted_date()) == 5


def test_latest_operation():
    """тест на количество разделов в виджете
    и на верное отображение первых символов"""
    assert len(latest_operation().split("\n\n")) == 6
    assert latest_operation()[2] == "."
