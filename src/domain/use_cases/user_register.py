from abc import ABC, abstractmethod
from typing import Dict


class UserRegisterInterface(ABC):
    @abstractmethod
    def create(self) -> Dict:
        pass
