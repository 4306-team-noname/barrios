from convert_case import snake_case
import importlib
import datetime
import numpy as np


def insert_model(name, fields, values):
    params_dict = {}

    for idx, f in np.ndenumerate(fields):
        key = snake_case(f)

        if key == "date" or key == "datedim" or key == "report_date":
            val = datetime.datetime.strptime(values[idx], "%m/%d/%Y").date()
        else:
            val = values[idx]
        print(f"{key}: {type(val)}: {val}")
        params_dict[key] = val

    ReturnClass = getattr(importlib.import_module(f".models.{name}"), name)
    # print(ReturnClass)
    insert_row = ReturnClass.create(params_dict)

    if insert_row["id"] is None:
        error_key = list(insert_row["errors"])[0]
        return {
            "ok": False,
            "error": insert_row["errors"][error_key],
            "error_field": error_key,
        }

    return {"ok": True, "value": insert_row["id"]}
