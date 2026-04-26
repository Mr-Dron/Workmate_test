import reports  #!!!Регистрирует отчеты!!!

from tabulate import tabulate
from reader import read_files
from utils import read_args
from config import get_report


def main() -> None:
    args = read_args()

    report_func = get_report(args.report)
    data = read_files(args.files)

    result = report_func(data)

    print(tabulate(result, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
