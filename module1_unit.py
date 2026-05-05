from abc import ABC, abstractmethod

class Unit(ABC):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    def add_spell(self, spell):
        self.spells.append(spell)
    
    def cast_spell(self, index):
        if index < 0 or index >= len(self.spells):
            raise IndexError("Нет заклинания с таким индексом")
        
        spell = self.spells[index]
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            raise Exception(f"Не хватает маны! Нужно {spell.mana_cost}, есть {self.mana}")