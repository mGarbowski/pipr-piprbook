from typing import Optional

from core.model import Message
from persistence.json_database import JsonDatabase


class FileSystemMessageRepository:
    def __init__(self, database: JsonDatabase):
        self.__database = database

    def get_message_by_id(self, message_id: str) -> Optional[Message]:
        return self.__database.get_item(message_id, Message)
