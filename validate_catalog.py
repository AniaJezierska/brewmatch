import json
from pathlib import Path

catalog_path = Path(__file__).with_name("machines.json")
machines = json.loads(catalog_path.read_text(encoding="utf-8"))

for machine in machines:
    width = machine["width_cm"]

    if width is None:
        print(f"{machine['name']}: width unknown")
    elif type(width) not in (int, float) or width <= 0:
        raise ValueError(f"{machine['name']}: width_cm must be positive or null")
    else:
        print(f"{machine['name']}: {width} cm")