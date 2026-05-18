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


# МОДУЛЬ 2: Класс Character

class Character(Unit):
    """Класс персонажа с поддержкой разных игровых классов."""

    VALID_CLASSES = ['warrior', 'mage', 'hunter']

    def __init__(self, strength, dexterity, constitution, wisdom,
                 intelligence, charisma, character_class):
        """
        Инициализация персонажа.

        Args:
            character_class: Класс персонажа ('warrior', 'mage', 'hunter')

        Raises:
            ValueError: Если передан неизвестный класс персонажа
        """
        super().__init__(strength, dexterity, constitution,
                         wisdom, intelligence, charisma)

        if character_class not in self.VALID_CLASSES:
            raise ValueError(
                f"Класс должен быть {self.VALID_CLASSES}, "
                f"получен {character_class}"
            )

        self.character_class = character_class
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self):
        """
        Максимальное здоровье персонажа.
        Формула: телосложение * 10 + сила // 2
        """
        return (self.constitution * 10) + (self.strength // 2)

    def calculate_damage(self):
        """Рассчитывает урон в зависимости от класса персонажа."""
        if self.character_class == 'warrior':
            # Сила * 2.2 + телосложение // 3
            return int((self.strength * 2.2) + (self.constitution // 3))
        elif self.character_class == 'mage':
            # Интеллект * 2.5 + мудрость // 2
            return int((self.intelligence * 2.5) + (self.wisdom // 2))
        elif self.character_class == 'hunter':
            # Ловкость * 1.9 + сила // 3
            return int((self.dexterity * 1.9) + (self.strength // 3))
        return 0

    def calculate_defense(self):
        """Рассчитывает защиту в зависимости от класса персонажа."""
        if self.character_class == 'warrior':
            # Телосложение * 1.8 + сила // 4
            return int((self.constitution * 1.8) + (self.strength // 4))
        elif self.character_class == 'mage':
            # Мудрость * 1.3 + интеллект // 6
            return int((self.wisdom * 1.3) + (self.intelligence // 6))
        elif self.character_class == 'hunter':
            # Ловкость * 1.6 + телосложение // 5
            return int((self.dexterity * 1.6) + (self.constitution // 5))
        return 0

    def calculate_max_mana(self):
        """Рассчитывает максимальную ману в зависимости от класса."""
        if self.character_class == 'warrior':
            # Интеллект + сила // 2
            return self.intelligence + (self.strength // 2)
        elif self.character_class == 'mage':
            # Интеллект * 3 + мудрость
            return (self.intelligence * 3) + self.wisdom
        elif self.character_class == 'hunter':
            # Ловкость * 1.5 + мудрость // 2
            return int((self.dexterity * 1.5) + (self.wisdom // 2))
        return 0


# МОДУЛЬ 3: Заклинания

class Spell(ABC):
    """Абстрактный класс для всех заклинаний."""

    def __init__(self, name, damage, mana_cost):
        """
        Инициализация заклинания.

        Args:
            name: Название заклинания
            damage: Базовый урон
            mana_cost: Стоимость в мане
        """
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        """Применяет заклинание и возвращает урон."""
        pass


class Fireball(Spell):
    """Огненный шар - урон 35, стоимость 15 маны."""

    def __init__(self):
        super().__init__("Огненный шар", 35, 15)

    def cast(self):
        return self.damage


class IceLance(Spell):
    """Ледяное копьё - урон 25, стоимость 10 маны."""

    def __init__(self):
        super().__init__("Ледяное копьё", 25, 10)

    def cast(self):
        return self.damage


class LightningBolt(Spell):
    """Разряд молнии - урон 40, стоимость 20 маны."""

    def __init__(self):
        super().__init__("Разряд молнии", 40, 20)

    def cast(self):
        return self.damage
