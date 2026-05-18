#!/usr/bin/env python3
"""
Игра от кота Василия
Ролевая игра с пошаговой боевой системой.
Содержит все модули в одном файле.
"""

from abc import ABC, abstractmethod

# МОДУЛЬ 1: Абстрактный класс Unit

class Unit(ABC):
    """Абстрактный базовый класс для всех игровых юнитов."""

    def __init__(self, strength, dexterity, constitution, wisdom,
                 intelligence, charisma):
        """
        Инициализация базовых характеристик юнита.

        Args:
            strength: Сила
            dexterity: Ловкость
            constitution: Телосложение
            wisdom: Мудрость
            intelligence: Интеллект
            charisma: Харизма
        """
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
        """Рассчитывает максимальное здоровье юнита."""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Рассчитывает базовый урон юнита."""
        pass

    @abstractmethod
    def calculate_defense(self):
        """Рассчитывает защиту юнита."""
        pass

    def add_spell(self, spell):
        """Добавляет заклинание в список юнита."""
        self.spells.append(spell)

    def cast_spell(self, index):
        """
        Применяет заклинание по индексу.

        Args:
            index: Индекс заклинания в списке

        Returns:
            int: Урон от заклинания

        Raises:
            IndexError: Если заклинания с таким индексом нет
            ValueError: Если не хватает маны
        """
        if index < 0 or index >= len(self.spells):
            raise IndexError("Нет заклинания с таким индексом")

        spell = self.spells[index]

        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            raise ValueError(
                f"Не хватает маны! Нужно {spell.mana_cost}, есть {self.mana}"
            )
