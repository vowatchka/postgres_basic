"""Модуль обработчиков исключений"""

import contextlib


@contextlib.contextmanager
def exc_handler():
    """
    Контекстный менеджер обработки исключения. Возбужденное исключение просто печатается (`print`).
    """
    try:
        yield
    except Exception as ex:
        print(ex)
