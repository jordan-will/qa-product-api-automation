# Product API Automation

API test automation project developed with Python, pytest, and requests to validate the DummyJSON Products API.

The project was created as a QA Automation portfolio project, focusing on API testing, test architecture, validation, mocking, fixtures, and CI/CD integration.

## Project Overview

The project automates tests for the main operations of the DummyJSON Products API:

* Retrieve the product list
* Retrieve a product by ID
* Validate a nonexistent product
* Create a product
* Update a product
* Delete a product

The test suite is divided into unit tests and API tests.

Unit tests validate the project components in isolation using mocks, while API tests communicate with the real DummyJSON API.

## Technologies

* Python 3.12
* pytest
* requests
* Git
* GitHub
* GitHub Actions

## API

The project uses the DummyJSON Products API.

Base URL:

```text
https://dummyjson.com
```

Endpoints covered:

| Method | Endpoint         | Purpose                      |
| ------ | ---------------- | ---------------------------- |
| GET    | `/products`      | Retrieve products            |
| GET    | `/products/{id}` | Retrieve a specific product  |
| GET    | `/products/{id}` | Validate nonexistent product |
| POST   | `/products/add`  | Create a product             |
| PUT    | `/products/{id}` | Update a product             |
| DELETE | `/products/{id}` | Delete a product             |

The write operations provided by DummyJSON are simulated and do not provide persistent database changes. Therefore, the tests validate the HTTP response and returned data rather than persistence.

## Project Architecture

The project separates HTTP communication, API-specific operations, data representation, validation, fixtures, and test scenarios.

```text
                         DummyJSON
                            |
                            v
                     +-------------+
                     | BaseClient  |
                     +------+------+
                            |
                            v
                  +-------------------+
                  |   ProductClient   |
                  +---------+---------+
                            |
                    +-------+-------+
                    |               |
                    v               v
                Response         Product
                    |
                    v
                API Tests
                    |
                    v
                Validators
```

### Components

#### BaseClient

Provides common HTTP operations:

* GET
* POST
* PUT
* DELETE
* URL construction
* Request timeout

The `BaseClient` does not contain product-specific rules or test assertions.

#### ProductClient

Provides operations specific to the Products API:

* `get_products()`
* `get_product()`
* `create_product()`
* `update_product()`
* `delete_product()`

It also transforms the response data of `get_product()` into a `Product` model.

#### Product Model

The `Product` dataclass represents the main product data used by the project:

```text
id
title
price
stock
```

The model follows the API field names directly.

#### Validators

The validation layer is responsible for checking:

* HTTP status codes
* JSON structure
* required fields
* field types
* positive values
* non-negative values
* product structure and business rules

Validators are independent from HTTP clients and fixtures.

#### Fixtures

`conftest.py` provides shared test resources:

* application settings
* `BaseClient`
* `ProductClient`
* product test data
* valid product payload

## Test Strategy

The project uses two test levels.

### Unit Tests

Unit tests validate the project components independently from the real API.

HTTP calls are replaced with mocks using `unittest.mock`.

```text
Mock
  |
  v
Project Component
  |
  v
Assertions
```

Unit tests cover:

* `BaseClient`
* `ProductClient`
* JSON-to-`Product` transformation
* validators
* test infrastructure
* configuration

The objective is to verify that the project's own components behave correctly without depending on network communication.

### API Tests

API tests communicate with the real DummyJSON API.

```text
Test
  |
  v
ProductClient
  |
  v
DummyJSON
  |
  v
Response
  |
  v
Validators
  |
  v
Assertions
```

API tests validate:

* HTTP status codes
* response structure
* required fields
* product data types
* product values
* positive scenarios
* negative scenarios

## API Test Scenarios

The API test suite covers the following scenarios:

| ID    | Scenario                     | Expected Result                             |
| ----- | ---------------------------- | ------------------------------------------- |
| API01 | Retrieve products            | HTTP 200 and valid list structure           |
| API02 | Validate returned products   | All returned products satisfy product rules |
| API03 | Retrieve product by ID       | Valid product data                          |
| API04 | Retrieve nonexistent product | HTTP 404                                    |
| API05 | Create product               | HTTP 201 and valid product data             |
| API06 | Update product               | HTTP 200 and updated product data           |
| API07 | Delete product               | HTTP 200 and deletion information           |

## Project Structure

```text
p2-product-api-automation/
|
├── .github/
│   └── workflows/
│       └── tests.yml
|
├── config/
│   ├── __init__.py
│   └── settings.py
|
├── src/
│   ├── __init__.py
│   ├── clients/
│   │   ├── __init__.py
│   │   ├── base_client.py
│   │   └── product_client.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   └── validators/
│       ├── __init__.py
│       ├── response_validator.py
│       └── product_validator.py
|
├── tests/
│   ├── api/
│   │   └── test_product_api.py
│   │
│   ├── unit/
│   │   ├── test_base_client.py
│   │   ├── test_product_client.py
│   │   ├── test_infrastructure.py
│   │   ├── test_settings.py
│   │   ├── test_smoke.py
│   │   └── test_validators.py
│   │
│   ├── data/
│   │   └── products.json
│   │
│   └── conftest.py
|
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Configuration

The project supports configuration through environment variables.

Example:

```env
API_BASE_URL=https://dummyjson.com
API_TIMEOUT=10
```

A `.env.example` file is included as a configuration reference.

The project also provides default values in `config/settings.py`, allowing the test suite to run without creating a local `.env` file.

The `.env` file is excluded from version control.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd p2-product-api-automation
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run only unit tests:

```bash
pytest tests/unit -v
```

Run only API tests:

```bash
pytest tests/api -v
```

## Continuous Integration

The project uses GitHub Actions to automatically execute the test suite.

The workflow is triggered by:

* Pushes
* Pull requests

The CI pipeline performs the following steps:

```text
Push / Pull Request
        |
        v
GitHub Actions
        |
        v
Ubuntu
        |
        v
Python 3.12
        |
        v
Install dependencies
        |
        v
pytest -v
        |
        v
Unit Tests + API Tests
        |
        v
PASS / FAIL
```

Workflow file:

```text
.github/workflows/tests.yml
```

The CI environment installs the dependencies from `requirements.txt` and executes the same test suite used locally.

Because the API tests communicate with the real DummyJSON service, their execution depends on the availability of that external API.

## Test Result

The complete test suite was successfully executed both locally and through GitHub Actions.

The CI pipeline completed successfully with all tests passing.

## Project Scope

This project intentionally focuses on API test automation fundamentals.

Included:

* API testing
* Unit testing
* Mocking
* Fixtures
* Test data
* Validation
* HTTP client abstraction
* Data modeling
* Git
* GitHub Actions
* CI test execution

Not included:

* UI automation
* Database testing
* Authentication
* Performance testing
* Security testing
* Docker
* Deployment
* Multiple environments
* Persistent test data management

These topics can be explored in future projects.

## Purpose

The main purpose of this project is to demonstrate practical QA Automation skills through a small, structured, and maintainable API automation framework.

The project emphasizes separation of responsibilities between clients, models, validators, fixtures, and tests, while integrating the test suite into a continuous integration pipeline.
