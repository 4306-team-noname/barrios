# from .UserDataEntry import UserDataEntry
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKey,
    IntegerField,
    Model,
    RESTRICT,
)


class InventoryMgmtSystemConsumables(Model):
    datedim = DateTimeField()
    ims_id = IntegerField(null=True)
    id_parent = IntegerField(null=True)
    id_path = CharField(max_length=200)
    tree_depth = IntegerField(null=True)
    tree = CharField(max_length=200)
    part_number = CharField(max_length=200)
    serial_number = IntegerField(null=True)
    location_name = CharField(max_length=200)
    original_ip_owner = CharField(max_length=200)
    current_ip_owner = CharField(max_length=200)
    operational_nomenclature = CharField(max_length=200)
    russian_name = CharField(max_length=200)
    english_name = CharField(max_length=200)
    barcode = CharField(max_length=200)
    quantity = IntegerField(null=True)
    width = FloatField(blank=True, null=True)
    height = FloatField(blank=True, null=True)
    length = FloatField(blank=True, null=True)
    diameter = FloatField(blank=True, null=True)
    calculated_volume = FloatField()
    stwg_ovrrd_vol = FloatField(blank=True, null=True)
    children_volume = FloatField(blank=True, null=True)
    stwg_ovrrd_chldrn_vol = FloatField(blank=True, null=True)
    ovrrd_notes = CharField()
    volume_notes = CharField()
    expire_date = DateTimeField(blank=True, null=True)
    launch = CharField(blank=True, null=True)
    type = CharField()
    hazard = CharField(blank=True, null=True)
    state = CharField()
    status = CharField()
    is_container = BooleanField()
    is_moveable = BooleanField()
    system = CharField()
    subsystem = CharField()
    action_date = DateTimeField()
    move_date = DateTimeField()
    fill_status = CharField(blank=True, null=True)
    category_id = ForeignKey("Category", to_field="category_id", on_delete=RESTRICT)
    category_name = CharField()

    class Meta:
        db_table = "inventory_mgmt_system_consumable"
