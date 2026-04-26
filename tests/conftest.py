import pytest
import tempfile
import os


@pytest.fixture
def data_file1():
    return (
        "test1,21.2,25,1240\n"
        "test2,24,24,4231\n"
        "test3,23.2,23,4102\n"
        "test4,13.2,23,2403\n"
        "test5,26,43,6321"
    )


@pytest.fixture
def data_file2():
    return (
        "test6,1.2,36,1430\n"
        "test7,34,42,3100\n"
        "test8,32.1,13,1020\n"
        "test9,33.6,21,943\n"
        "test0,23,55,4792"
    )


@pytest.fixture
def multiple_csv_file(data_file1, data_file2):
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, "file1.csv")
        file2 = os.path.join(tmpdir, "file2.csv")

        with open(file1, "w") as file:
            file.write(f"title,ctr,retention_rate,views\n{data_file1}")

        with open(file2, "w") as file:
            file.write(f"title,ctr,retention_rate,views\n{data_file2}")

        yield [file1, file2]
