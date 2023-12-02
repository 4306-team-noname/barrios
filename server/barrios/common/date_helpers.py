from datetime import date, datetime


def get_date_object(date_string: str) -> date:
    return datetime.strptime(date_string, "%m/%d/%Y").date()


def get_datetime_object(datetime_string: str) -> datetime:
    return datetime.strptime(datetime_string, "%m/%d/%Y %H:%M")


def get_date_string(date: date) -> str:
    return date.strftime("%m/%d/%Y")


def get_datetime_string(datetime: datetime) -> str:
    return datetime.strftime("%m/%d/%Y %H:%M")
