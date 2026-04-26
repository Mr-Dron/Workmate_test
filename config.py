REPORTS = dict()


def register_report(name):
    def decorator(func):
        REPORTS[name] = func
        return func

    return decorator


def get_report(name: str):
    try:
        return REPORTS[name]
    except KeyError:
        raise ValueError(f"Unknown report name: {name}")


def get_all_reports():
    return list(REPORTS.keys())
