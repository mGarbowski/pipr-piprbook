"""Generating and validating IDs"""

import re
from uuid import uuid1


def generate_uuid() -> str:
    """Generate a universaly unique id"""
    return str(uuid1())


def is_uuid(uuid: str) -> bool:
    """Check if string is a correct uuid

    :param uuid: string to check
    """
    uuid_pattern = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
    return bool(re.fullmatch(uuid_pattern, uuid))
