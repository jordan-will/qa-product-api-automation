import pytest
from unittest.mock import Mock

from src.validators.product_validator import validate_product
from src.validators.response_validator import (
    validate_field_types,
    validate_json_structure,
    validate_non_negative,
    validate_positive,
    validate_required_fields,
    validate_status_code,
)


# Status code


def test_validate_status_code_accepts_expected_status():
    response = Mock()
    response.status_code = 200

    validate_status_code(response, 200)


def test_validate_status_code_rejects_unexpected_status():
    response = Mock()
    response.status_code = 404

    with pytest.raises(AssertionError):
        validate_status_code(response, 200)


# JSON structure


def test_validate_json_structure_accepts_expected_type():
    data = {
        "id": 1,
        "title": "Example Product",
    }

    validate_json_structure(data, dict)


def test_validate_json_structure_rejects_unexpected_type():
    data = [
        {
            "id": 1,
            "title": "Example Product",
        }
    ]

    with pytest.raises(AssertionError):
        validate_json_structure(data, dict)


# Required fields


def test_validate_required_fields_accepts_complete_data():
    data = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
        "stock": 20,
    }

    validate_required_fields(
        data,
        ["id", "title", "price", "stock"],
    )


def test_validate_required_fields_rejects_missing_field():
    data = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
    }

    with pytest.raises(AssertionError):
        validate_required_fields(
            data,
            ["id", "title", "price", "stock"],
        )


# Field types


def test_validate_field_types_accepts_correct_types():
    data = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
        "stock": 20,
    }

    validate_field_types(
        data,
        {
            "id": int,
            "title": str,
            "price": float,
            "stock": int,
        },
    )


def test_validate_field_types_rejects_incorrect_type():
    data = {
        "id": 1,
        "title": "Example Product",
        "price": "99.99",
        "stock": 20,
    }

    with pytest.raises(AssertionError):
        validate_field_types(
            data,
            {
                "id": int,
                "title": str,
                "price": float,
                "stock": int,
            },
        )


# Value validators


def test_validate_positive_accepts_positive_value():
    validate_positive(10)


def test_validate_positive_rejects_zero_and_negative_values():
    with pytest.raises(AssertionError):
        validate_positive(0)

    with pytest.raises(AssertionError):
        validate_positive(-1)


def test_validate_non_negative_accepts_zero_and_positive_values():
    validate_non_negative(0)
    validate_non_negative(10)


def test_validate_non_negative_rejects_negative_value():
    with pytest.raises(AssertionError):
        validate_non_negative(-1)


# Product validator


def test_validate_product_accepts_valid_product():
    product = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
        "stock": 20,
    }

    validate_product(product)


def test_validate_product_rejects_invalid_id():
    product = {
        "id": 0,
        "title": "Example Product",
        "price": 99.99,
        "stock": 20,
    }

    with pytest.raises(AssertionError):
        validate_product(product)


def test_validate_product_rejects_invalid_price():
    product = {
        "id": 1,
        "title": "Example Product",
        "price": 0.0,
        "stock": 20,
    }

    with pytest.raises(AssertionError):
        validate_product(product)


def test_validate_product_rejects_negative_stock():
    product = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
        "stock": -1,
    }

    with pytest.raises(AssertionError):
        validate_product(product)


def test_validate_product_rejects_missing_field():
    product = {
        "id": 1,
        "title": "Example Product",
        "price": 99.99,
    }

    with pytest.raises(AssertionError):
        validate_product(product)