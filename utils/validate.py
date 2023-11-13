"""Custom validation functions."""

import os


def validate_env_var(var: str) -> None:
    """Check if environment variable is None."""
    error = f"environment variable {var} is not set"
    if os.getenv(var) is None:
        raise TypeError(error)
