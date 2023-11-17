from django.db.models import CharField, IntegerField, Model


class Category(Model):
    category_id = IntegerField(primary_key=True)
    category_name = CharField(max_length=200, unique=True, null=True, blank=True)
    rate_category = CharField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        db_table = "categories"
