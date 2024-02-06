from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(
    ABC
):  # ABC funciona para mostrar ao interpretador que se trata de uma classe abstrata.
    """Interface to FindPet use case"""

    @abstractclassmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractclassmethod
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")

    @abstractclassmethod
    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_name")
