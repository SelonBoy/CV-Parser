# parser/validator.py
import json
from models.schema import CVSchema
from pydantic import ValidationError

def validate_and_format(raw_json_str: str) -> dict:
    """
    Menerima string JSON mentah dari LLM,
    memvalidasi strukturnya, dan mengembalikan dict bersih.
    """
    try:
        # Bersihkan output LLM jika ada prefix/suffix
        raw_json_str = raw_json_str.strip()
        if raw_json_str.startswith("```"):
            raw_json_str = raw_json_str.split("```")[1]
            if raw_json_str.startswith("json"):
                raw_json_str = raw_json_str[4:]

        data = json.loads(raw_json_str)
        cv = CVSchema(**data)           # Validasi via Pydantic
        return cv.model_dump()          # Kembalikan sebagai dict bersih

    except (json.JSONDecodeError, ValidationError) as e:
        return {"error": str(e), "raw": raw_json_str}