from uuid import uuid1


def generate_uuid() -> str:
    return str(uuid1())
