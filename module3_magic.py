from abc import ABC, abstractmethod
from module1_unit import Unit
from module2_character import Character

class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    
    @abstractmethod
    def cast(self):
        pass

