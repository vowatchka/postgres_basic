"""Модуль вспомогательных функций для таблиц SQLAlchemy"""

from collections.abc import Iterable
from typing import Any

from sqlalchemy.engine import CursorResult, Row
from sqlalchemy.sql.base import ImmutableColumnCollection
from tabulate import tabulate

from IPython.display import display, HTML


def table(table_data: Any, headers: tuple = ()):
    """
    Вывод таблицы в формате HTML.

    :param table_data: данные для выводимой таблицы
    :param headers: заголовки выводимой таблицы
    """
    html_table = tabulate(table_data, headers=headers, tablefmt="html", floatfmt="f")
    display(HTML(html_table))


def sqlalchemy_table(rows: CursorResult | Iterable[Row]):
    """
    Вывод строк, получаемых через SQLAlchemy, в виде таблицы в формате HTML.

    :param rows: строки, полученные через SQLAlchemy
    """
    headers = ()
    table_data: list[tuple[Any, ...]] = []

    for idx, row in enumerate(rows):
        if idx == 0:
            headers = tuple(dict(row).keys())

        table_data.append(tuple(row))

    table(table_data, headers)


def clear_declarative_registry(registry: Any):
    """
    Декоратор декларативных классов SQLAlchemy для очистки регистра классов

    :param registry: регистр классов. Должен поддерживать метод `clear()`
    """
    def class_decorator(cls):
        return cls

    registry.clear()

    return class_decorator


def all_cols(table: Any) -> ImmutableColumnCollection:
    """
    Функция возврата всех столбцов таблицы SQLAlchemy

    :param table: таблица SQLAlchemy
    """
    return table.__table__.columns


class AllColumnsMixin:
    @classmethod
    def all_cols(cls):
        return all_cols(cls)
