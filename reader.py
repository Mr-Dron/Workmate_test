import csv

from typing import List, Dict


def read_files(files_path: List[str]) -> List[Dict[str, str]]:
    data = []
    for file_path in files_path:
        try:
            with open(file=file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                data.extend(list(reader))
        except OSError as exc:
            print(f"Error reading {file_path}: {exc}")

    return data
