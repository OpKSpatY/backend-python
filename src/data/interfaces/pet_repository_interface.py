from abc import ABC, abstractclassmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Interface to pet Repository"""

    @abstractclassmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractclassmethod
    def select_pet(self, pet_id: int, user_id: int = None) -> List[Pets]:
        """abstract method"""

        raise Exception("Method not implemented")
