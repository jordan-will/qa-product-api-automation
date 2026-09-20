from requests import Response


def validate_status_code(
    response: Response,
    expected_status: int,
) -> None:
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but received {response.status_code}."
    )


def validate_json_structure(
    data: object,
    expected_type: type,
) -> None:
    assert isinstance(data, expected_type), (
        f"Expected JSON structure of type {expected_type.__name__}, "
        f"but received {type(data).__name__}."
    )


def validate_required_fields(
    data: dict,
    fields: list[str],
) -> None:
    for field in fields:
        assert field in data, (
            f"Required field '{field}' is missing."
        )


def validate_field_types(
    data: dict,
    expected_types: dict[str, type],
) -> None:
    for field, expected_type in expected_types.items():
        assert isinstance(data[field], expected_type), (
            f"Field '{field}' expected type "
            f"{expected_type.__name__}, "
            f"but received {type(data[field]).__name__}."
        )

def validate_positive(value: int | float) -> None:
    assert value > 0, (
        f"Expected a positive value, but received {value}."
    )

def validate_non_negative(value: int | float) -> None:
    assert value >= 0, (
        f"Expected a non-negative value, but received {value}."
    )