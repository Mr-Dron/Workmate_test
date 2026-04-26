import argparse

from argparse import Namespace
from config import get_all_reports


def read_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True, help="Список CSV файлов")

    parser.add_argument(
        "--report", choices=get_all_reports(), required=True, help="Названия отчетов"
    )

    args = parser.parse_args()

    return args
