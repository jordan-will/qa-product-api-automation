import os

BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://dummyjson.com",
)

TIMEOUT = int(
    os.getenv(
        "API_TIMEOUT",
        "10",
    )
)