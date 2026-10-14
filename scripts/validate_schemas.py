"""Validate bundled schemas and their examples without contacting external services."""
import json
from pathlib import Path

from jsonschema import FormatChecker
from jsonschema.validators import validator_for

ROOT = Path(__file__).resolve().parents[1] / "schemas"


def main():
    for schema_path in sorted(ROOT.glob("*.schema.json")):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator_type = validator_for(schema)
        validator_type.check_schema(schema)
        validator = validator_type(schema, format_checker=FormatChecker())
        example = ROOT / "examples" / schema_path.name.replace(".schema.json", ".example.json")
        validator.validate(json.loads(example.read_text(encoding="utf-8")))
        print(f"validated {schema_path.name} and {example.name}")


if __name__ == "__main__":
    main()
