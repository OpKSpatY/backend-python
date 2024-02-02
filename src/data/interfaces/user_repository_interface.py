from abc import ABC, abstractclassmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to pet Repository"""

    @abstractclassmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractclassmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstract method"""

        raise Exception("Method not implemented")
