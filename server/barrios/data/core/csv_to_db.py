from __future__ import annotations
from django.db.models import QuerySet
from django.db.models.base import ModelBase


def csv_to_db(
    model: ModelBase, filepath: str, mapping: dict[str, str] | None = None
) -> QuerySet:
    result = model.objects.from_csv(
        filepath,
        encoding="utf-8",
        mapping=mapping,
        drop_constraints=False,
        drop_indexes=False,
    )
    return result
