"""Модуль вывода таблиц в Jupyter Notebook"""

from collections.abc import Iterable
from typing import Any

from sqlalchemy.engine import CursorResult, Row
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
