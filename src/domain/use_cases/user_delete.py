from abc import ABC, abstractmethod
from typing import Dict


class UserDeleteInterface(ABC):
    @abstractmethod
    def delete(self) -> Dict:
        pass
