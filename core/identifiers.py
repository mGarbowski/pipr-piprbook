"""Generating IDs."""

from uuid import uuid1


def generate_uuid() -> str:
    """Generate a universaly unique id."""
    return str(uuid1())
