from cases import to_snake
import importlib
import datetime

from django.db.models import QuerySet
from data.models import Category


def snake_keys(d):
    new_dict = {}
    for key in d.keys():
        new_dict[to_snake(key)] = d[key]
    return new_dict


def vals_to_date(d):
    new_dict = {}
    for key in d.keys():
        if key == "date" or key == "datedim" or key == "report_date":
            new_dict[key] = datetime.datetime.strptime(d[key], "%m/%d/%Y").date()
        else:
            new_dict[key] = d[key]
    return new_dict


def get_category(id):
    category = Category.objects.get(category_id=id)
    return category


def is_cat_model(model_name):
    cat_models = [
        "ImsConsumablesCategoryLookup",
        "InventoryMgmtSystemConsumables",
        "RatesDefinition",
        "StoredItemsOnlyInventoryMgmtSystemConsumables",
        "ThresholdLimitsDefinition",
    ]
    return model_name in cat_models


def create_category_model(model_name, model_dict):
    cat: Category = None
    q: QuerySet = None

    if model_name == "ImsConsumablesCategoryLookup":
        cat = Category.objects.get(category_id=model_dict["category_id"])
    elif model_name == "InventoryMgmtSystemConsumables":
        cat = Category.objects.get(category_id=model_dict["category_id"])
    elif model_name == "StoredItemsOnlyInventoryMgmtSystemConsumables":
        cat = Category.objects.get(category_id=model_dict["category_id"])
    elif model_name == "RatesDefinition":
        cat = Category.objects.get(rate_category=model_dict["rate_category"])
    elif model_name == "ThresholdLimitsDefinition":
        cat = Category.objects.get(category_name=model_dict["threshold_category"])

    if cat is not None:
        model_dict["category_id"] = cat
        InsertionModel = getattr(
            importlib.import_module(f"data.models.{model_name}"), model_name
        )
    else:
        model_dict["category_id"] = None
        InsertionModel = InsertionModel = getattr(
            importlib.import_module(f"data.models.{model_name}"), model_name
        )

    q = InsertionModel.objects.update_or_create(**model_dict)

    return q


def insert_model(name, rows):
    converted = [vals_to_date(snake_keys(d)) for d in rows]
    print(converted)

    if is_cat_model(name):
        for row in converted:
            # check to see whether this model needs a category instance
            create_category_model(name, row)
    else:
        ReturnClass = getattr(importlib.import_module(f"data.models.{name}"), name)

        instance_list = [ReturnClass(**d) for d in converted]
        # print(instance_list)
        queryset = ReturnClass.objects.bulk_create(instance_list, batch_size=999)
        # print(queryset)
    # # instance = ReturnClass(**params_dict)
    # insert_result = ReturnClass.objects.create(**params_dict)
    #
    # print(insert_result)  # should return a QuerySet
    #
    # if insert_result is not None:
    #     return {"ok": True, "value": insert_result}
    # else:
    return {
        "ok": False,
        "error": "There was a problem inserting the model into the database.",
    }
