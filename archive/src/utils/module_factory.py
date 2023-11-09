from importlib import import_module
from typing import Optional, Sequence

DEFAULT_MODULES = [
    "modules.dashboard.controller",
    "modules.flightplan.controller",
    "modules.forecast.controller",
    "modules.main.controller",
    "modules.usage.controller",
    "modules.userdata.controller",
]

PROTECTED_MODULES = [
    "modules.dashboard.controller",
    "modules.flightplan.controller",
    "modules.forecast.controller",
    "modules.usage.controller",
    "modules.userdata.controller",
]


def import_app_modules(init_modules: Optional[Sequence[str]] = None):
    app_modules = []
    if not init_modules:
        init_modules = DEFAULT_MODULES

    for module_name in init_modules:
        app_modules.append(import_module(module_name))

    return app_modules
