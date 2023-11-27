# from .UserDataEntry import UserDataEntry
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    RESTRICT,
)
from postgres_copy import CopyManager
from .CustomFields import EmptyStringToNoneFloatField, EmptyStringToNoneIntegerField
from django.utils.timezone import make_aware
from datetime import datetime
from data.models import ImsModel
from data.core.managers import EmptyKeywordManager


class ImsManager(EmptyKeywordManager):
    date_fields = ["datedim", "expire_date", "action_date", "move_date"]

    def create(self, *args, **kwargs):
        newargs = {}
        for key in kwargs.keys():
            if key == "id":
                newargs["ims_id"] = kwargs[key]
            else:
                newargs[key] = kwargs[key]
            if key in self.date_fields:
                if len(kwargs[key]) > 0:
                    newargs[key] = make_aware(
                        datetime.strptime(kwargs[key], "%m/%d/%Y %H:%M")
                    )
                else:
                    newargs[key] = None
        del kwargs["id"]
        super().create(*args, **newargs)


class InventoryMgmtSystemConsumables(Model):
    datedim = DateTimeField()
    ims_id = EmptyStringToNoneIntegerField(null=True)
    id_parent = EmptyStringToNoneIntegerField(null=True)
    id_path = CharField(max_length=200)
    tree_depth = EmptyStringToNoneIntegerField(null=True)
    tree = CharField(max_length=200, blank=True, null=True)
    part_number = CharField(max_length=200, blank=True, null=True)
    serial_number = CharField(blank=True, null=True)
    location_name = CharField(max_length=200, blank=True, null=True)
    original_ip_owner = CharField(max_length=200, blank=True, null=True)
    current_ip_owner = CharField(max_length=200, blank=True, null=True)
    operational_nomenclature = CharField(max_length=200, blank=True, null=True)
    russian_name = CharField(max_length=200, blank=True, null=True)
    english_name = CharField(max_length=200, blank=True, null=True)
    barcode = CharField(max_length=200, blank=True, null=True)
    quantity = EmptyStringToNoneIntegerField(null=True)
    width = EmptyStringToNoneFloatField(blank=True, null=True)
    height = EmptyStringToNoneFloatField(blank=True, null=True)
    length = EmptyStringToNoneFloatField(blank=True, null=True)
    diameter = EmptyStringToNoneFloatField(blank=True, null=True)
    calculated_volume = EmptyStringToNoneFloatField(blank=True, null=True)
    stwg_ovrrd_vol = EmptyStringToNoneFloatField(blank=True, null=True)
    children_volume = EmptyStringToNoneFloatField(blank=True, null=True)
    stwg_ovrrd_chldrn_vol = EmptyStringToNoneFloatField(blank=True, null=True)
    ovrrd_notes = CharField(blank=True, null=True)
    volume_notes = CharField(blank=True, null=True)
    expire_date = DateTimeField(blank=True, null=True)
    launch = CharField(blank=True, null=True)
    type = CharField(blank=True, null=True)
    hazard = CharField(blank=True, null=True)
    state = CharField(blank=True, null=True)
    status = CharField(blank=True, null=True)
    is_container = BooleanField(blank=True, null=True)
    is_moveable = BooleanField(blank=True, null=True)
    system = CharField(blank=True, null=True)
    subsystem = CharField(blank=True, null=True)
    action_date = DateTimeField(blank=True, null=True)
    move_date = DateTimeField(blank=True, null=True)
    fill_status = CharField(blank=True, null=True)
    category = ForeignKey("Category", to_field="category_id", on_delete=RESTRICT)
    category_name = CharField(blank=True, null=True)

    objects = ImsManager()

    class Meta:
        db_table = "inventory_mgmt_system_consumable"
