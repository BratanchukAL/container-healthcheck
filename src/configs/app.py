from typing import List

from marshmallow.validate import OneOf

from configs.env import env


DEBUG = env.bool("DEBUG", False)

MODE = env.str(
    "MODE",
    validate=OneOf(
        ("worker", "manager",),
        error="MODE must be one of: {choices}"
    )
)
# BACKEND_SECRET_KEY = env.str("BACKEND_SECRET_KEY")
# BACKEND_ALLOWED_HOSTS: List[str] = env.list("BACKEND_ALLOWED_HOSTS")
# SERVER_BACKEND_URL: str = env.str("SERVER_BACKEND_URL")
