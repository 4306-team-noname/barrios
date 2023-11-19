from django.db.models import Model


def generic_serializer(
    instances: list,
    exclude_models: list = None,
    exclude_fields: list = None,
) -> list:
    def get_fields(model: Model = None, fields: dict = None) -> dict:
        if not fields:
            fields = {}
            for f in model._meta.fields:
                if not f.is_relation and f.name in exclude_fields:
                    continue
                fields[f.name] = getattr(model, f.name)

        for name, value in fields.items():
            if not isinstance(value, Model):
                continue
            # Replace the excluded related model field with their primary key value
            # Instead of storing the `model.__str__()` value, it shows the model.pk
            # if it is in `exclude_models`
            fields[name] = (
                getattr(value, "pk") if name in exclude_models else get_fields(value)
            )
        return fields

    return [get_fields(instance) for instance in instances]
