from datetime import date


def get_flightplan_deltas(date_list: list[date]) -> list[int]:
    days_list = []
    for idx, d1 in enumerate(date_list):
        j = idx + 1
        if j < len(date_list):
            d2 = date_list[j]
            delta = d2 - d1
            days_list.append(delta.days)
    return days_list
