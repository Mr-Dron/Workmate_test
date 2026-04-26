from reader import read_files


def test_reader(multiple_csv_file, data_file1, data_file2):
    result = read_files(multiple_csv_file)

    assert len(result) == (len(data_file1.split("\n")) + len(data_file2.split("\n")))

    for row in result:
        assert "title" in row


def test_only_invalid_reader(capsys, multiple_csv_file, data_file1, data_file2):
    result = read_files(["invalip_file_path.csv"])
    captured = capsys.readouterr()

    assert "Error reading invalip_file_path.csv:" in captured.out
    assert result == []


def test_invalid_with_valid_reader(capsys, multiple_csv_file, data_file1, data_file2):
    files_path = multiple_csv_file + ["invalip_file_path.csv"]
    result = read_files(files_path)
    captured = capsys.readouterr()

    assert "Error reading invalip_file_path.csv:" in captured.out
    assert len(result) > 0
