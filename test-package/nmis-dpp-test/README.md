# Digital Product Passport

A modular Python package that enables manufacturing companies to create interoperable Digital Product Passports (DPPs) by mapping their existing business data to standardized DPP data models using automated semantic matching and intuitive configuration tools.

---
## Package Layout
dpp_passport/ \n
├── dpp_passport/ \n
│   ├── __init__.py \n
│   ├── model.py         # Core models for DPP layers \n
│   ├── part_class.py    # Universal part class set \n
│   ├── utils.py         # Any helper functions \n
├── tests/ \n
│   ├── test_model.py \n
│   ├── test_part_class.py \n
├── pyproject.toml \n
├── README.md \n

---

## Requirements
- Python 3.7+
- No external dependencies (uses Python dataclasses and standard library)

---

## Installation
### From PyPI
pip install nmis-dpp-test
### From Source
git clone https://github.com/AnmolK-NMIS/dpp-test.git
cd dpp-passport
pip install .


---

## Usage Example

Create a simple digital product passport with identity, structure, and key classes:

```
from dpp_passport.model import (
    IdentityLayer, StructureLayer, LifecycleLayer,
    RiskLayer, SustainabilityLayer, ProvenanceLayer, DigitalProductPassport
)
from dpp_passport.part_class import Actuator, Sensor, PowerConversion

# Example parts
motor = Actuator(part_id="A001", name="Motor", type="Actuator", torque=2.5, speed=1500, duty_cycle=80, voltage=48, properties={})
sensor = Sensor(part_id="S001", name="Temp Sensor", type="Sensor", range=255, accuracy=0.01, drift=0.001, signal_type="analog", properties={})
psu = PowerConversion(part_id="P001", name="PSU", type="PowerConversion", input_voltage=230, output_voltage=48, properties={})

# Layers
identity = IdentityLayer(
    global_ids={"gtin": "1234567890", "serial": "XYZ123"},
    make_model={"brand": "Acme", "model": "SuperWidget", "hw_rev": "1.0", "fw_rev": "1.2"},
    ownership={"manufacturer": "Acme Corp", "owner": "John", "operator": "Service Inc", "location": "Berlin"},
    conformity=["CE", "RoHS"]
)
structure = StructureLayer(
    hierarchy={"product": "Widget", "components": [motor, sensor, psu]},
    parts=[motor, sensor, psu],
    interfaces=[{"type": "electrical", "details": {"voltage": 48}}],
    materials=[],
    bom_refs=[]
)
lifecycle = LifecycleLayer(manufacture={}, use={}, serviceability={}, events=[], end_of_life={})
risk = RiskLayer(criticality={}, fmea=[], security={})
sustainability = SustainabilityLayer(mass=10.0, energy={}, recycled_content={}, remanufacture={})
provenance = ProvenanceLayer(signatures=[], trace_links=[])

# Assemble passport
dpp = DigitalProductPassport(
    identity=identity,
    structure=structure,
    lifecycle=lifecycle,
    risk=risk,
    sustainability=sustainability,
    provenance=provenance
)

print(dpp)
```
