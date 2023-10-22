from emmett.orm import Model, Field, belongs_to

class StoredItemsOnlyInventoryMgmtSystemConsumablesEntry(Model):
    tablename = 'stored_items_only_inventory_mgmt_system_consumables'
    belongs_to('upload')

    datedim = Field.text()
    id = Field.int()
    id_parent = Field.int()
    id_path = Field.text()
    tree_depth = Field.int()
    tree = Field.text()
    part_number = Field.text()
    serial_number = Field.int()
    location_name = Field.text()
    original_ip_owner = Field.text()
    current_ip_owner = Field.text()
    operational_nomenclature = Field.text()
    russian_name = Field.text()
    english_name = Field.text()
    barcode = Field.text()
    quantity = Field.int()
    width = Field.float()
    height = Field.float()
    length = Field.float()
    diameter = Field.float()
    calculated_volume = Field.float()
    stwg_ovrrd_vol = Field.float()
    children_volume = Field.float()
    stwg_ovrrd_chldrn_vol = Field.float()
    ovrrd_notes = Field.text()
    volume_notes = Field.text()
    expire_date = Field.text()
    launch = Field.text()
    type = Field.text()
    hazard = Field.text()
    state = Field.text()
    status = Field.text()
    is_container = Field.int()
    is_moveable = Field.int()
    system = Field.text()
    subsystem = Field.text()
    action_date = Field.text()
    move_date = Field.text()
    fill_status = Field.text()
    categoryID = Field.text()
    category_name = Field.text()


    validation = {
        'datedim': {'presence': True},
        'id': {'presence': True},
        'id_parent': {'presence': True},
        'id_path': {'presence': True},
        'tree_depth': {'presence': True},
        'tree': {'presence': True},
        'part_number': {'presence': True},
        'serial_number': {'presence': True},
        'location_name': {'presence': True},
        'original_ip_owner': {'presence': True},
        'current_ip_owner': {'presence': True},
        'operational_nomenclature': {'presence': True},
        'russian_name': {'presence': True},
        'english_name': {'presence': True},
        'barcode': {'presence': True},
        'quantity': {'presence': True},
        'width': {'presence': True},
        'height': {'presence': True},
        'length': {'presence': True},
        'diameter': {'presence': True},
        'calculated_volume': {'presence': True},
        'stwg_ovrrd_vol': {'presence': True},
        'children_volume': {'presence': True},
        'stwg_ovrrd_chldrn_vol': {'presence': True},
        'ovrrd_notes': {'presence': True},
        'volume_notes': {'presence': True},
        'type': {'presence': True},
        'state': {'presence': True},
        'status': {'presence': True},
        'is_container': {'presence': True},
        'is_moveable': {'presence': True},
        'action_date': {'presence': True},
        'move_date': {'presence': True},
        'categoryID': {'presence': True},
        'category_name': {'presence': True}
    }