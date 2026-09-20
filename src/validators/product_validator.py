from src.validators.response_validator import (
    validate_field_types,
    validate_json_structure,
    validate_non_negative,
    validate_positive,
    validate_required_fields,
)


def validate_product(data: dict) -> None:
    validate_json_structure(data, dict)

    validate_required_fields(
        data,
        ["id", "title", "price", "stock"],
    )

    validate_field_types(
        data,
        {
            "id": int,
            "title": str,
            "price": float,
            "stock": int,
        },
    )

    validate_positive(data["id"])
    validate_positive(data["price"])
    validate_non_negative(data["stock"])