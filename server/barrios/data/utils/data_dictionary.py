data_dictionary = {
    "ims_consumables_category_lookup": {
        "model_name": "ImsConsumablesCategoryLookup",
        "columns": {
            "category_name": "object",
            "categoryID": "int64",
            "module_name": "object",
            "moduleID": "int64",
            "unique_cat_mod_ID": "object",
        },
    },
    "iss_flight_plan": {
        "model_name": "IssFlightPlan",
        "columns": {
            "datedim": "object",
            "vehicle_name": "object",
            "port_name": "object",
            "vehicle_type": "object",
            "eva_name": "object",
            "eva_type": "object",
            "eva_accuracy": "object",
            "event": "object",
        },
    },
    "iss_flight_plan_crew": {
        "model_name": "IssFlightPlanCrew",
        "columns": {
            "datedim": "object",
            "nationality_category": "object",
            "crew_count": "int64",
        },
    },
    "iss_flight_plan_crew_nationality_lookup": {
        "model_name": "IssFlightPlanCrewNationalityLookup",
        "columns": {
            "nationality": "object",
            "is_usos_crew": "int64",
            "is_rsa_crew": "int64",
        },
    },
    "rates_definition": {
        "model_name": "RatesDefinition",
        "columns": {
            "rate_category": "object",
            "affected_consumable": "object",
            "rate": "float64",
            "units": "object",
            "type": "object",
            "efficiency": "int64",
        },
    },
    "rsa_consumable_water_summary": {
        "model_name": "RsaConsumableWaterSummary",
        "columns": {
            "Report Date": "object",
            "Remain. Potable (liters)": "float64",
            "Remain. Technical (liters)": "float64",
            "Remain. Rodnik (liters)": "float64",
        },
    },
    "tank_capacity_definition": {
        "model_name": "TankCapacityDefinition",
        "columns": {
            "tank_category": "object",
            "tank_capacity": "float64",
            "units": "object",
        },
    },
    "thresholds_limits_definition": {
        "model_name": "ThresholdsLimitsDefinition",
        "columns": {
            "threshold_category": "object",
            "threshold_value": "float64",
            "threshold_owner": "object",
            "units": "object",
        },
    },
    "us_rs_weekly_consumables_gas_summary": {
        "model_name": "UsRsWeeklyConsumableGasSummary",
        "columns": {
            "Date": "object",
            "USOS O2 (kg)": "float64",
            "RS O2 (kg)": "float64",
            "US N2 (kg)": "float64",
            "RS N2 (kg)": "float64",
            "Adjusted O2 (kg)": "float64",
            "Adjusted N2 (kg)": "float64",
            "Resupply O2 (kg)": "float64",
            "Resupply N2 (kg)": "float64",
            "Resupply Air (kg)": "float64",
        },
    },
    "us_weekly_consumable_water_summary": {
        "model_name": "UsWeeklyConsumableWaterSummary",
        "columns": {
            "Date": "object",
            "Corrected Potable (L)": "float64",
            "Corrected Technical  (L)": "float64",
            "Corrected Total (L)": "float64",
            "Resupply Potable (L)": "float64",
            "Resupply Technical (L)": "float64",
            "Corrected Predicted (L)": "float64",
        },
    },
    "inventory_mgmt_system_consumable": {
        "model_name": "InventoryMgmtSystemConsumables",
        "columns": {
            "datedim": "object",
            "id": "int64",
            "id_parent": "int64",
            "id_path": "object",
            "tree_depth": "int64",
            "tree": "object",
            "part_number": "object",
            "serial_number": "int64",
            "location_name": "object",
            "original_ip_owner": "object",
            "current_ip_owner": "object",
            "operational_nomenclature": "object",
            "russian_name": "object",
            "english_name": "object",
            "barcode": "object",
            "quantity": "int64",
            "width": "float64",
            "height": "float64",
            "length": "float64",
            "diameter": "float64",
            "calculated_volume": "float64",
            "stwg_ovrrd_vol": "float64",
            "children_volume": "float64",
            "stwg_ovrrd_chldrn_vol": "float64",
            "ovrrd_notes": "object",
            "volume_notes": "object",
            "expire_date": "object",
            "launch": "object",
            "type": "object",
            "hazard": "object",
            "state": "object",
            "status": "object",
            "is_container": "bool",
            "is_moveable": "bool",
            "system": "object",
            "subsystem": "object",
            "action_date": "object",
            "move_date": "object",
            "fill_status": "object",
            "categoryID": "int64",
            "category_name": "object",
        },
    },
}
