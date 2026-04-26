from typing import List, Dict

from config import register_report


@register_report("clickbait")
def clickbait_report(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    data_list = []

    for row in data:
        # при условии задания, что данные файла всегда валидны
        if float(row["ctr"]) > 15 and float(row["retention_rate"]) < 40:
            data_list.append(
                {
                    "title": row["title"],
                    "ctr": float(row["ctr"]),
                    "retention_rate": float(row["retention_rate"]),
                }
            )

    return sorted(data_list, key=lambda x: x["ctr"], reverse=True)
