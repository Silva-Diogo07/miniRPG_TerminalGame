import random
from .constants import REQUIRED_STAMINA_TO_SPECIAL_ATTACK


class Character:
    def __init__(self, name, hp, damage, weapon, agility, stamina):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.weapon = weapon
        self.agility = agility
        self.stamina = stamina
        self.is_defending = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage_amount):
        if self.is_defending:
            damage_amount //= 2
            self.is_defending = False

        self.hp -= damage_amount

        if self.hp <= 0:
            self.hp = 0
            return f"{self.name} took {damage_amount} damage and died."

        return f"{self.name} took {damage_amount} damage and now has {self.hp} HP."

    def dodged(self):
        return random.randint(1, 100) <= self.agility

    def attack(self, target):
        if target.dodged():
            return f"{target.name} dodged {self.name}'s attack."

        return f"{self.name} attacks {target.name} with {self.weapon}.\n{target.take_damage(self.damage)}"

    def special_attack(self, target):
        if self.stamina >= REQUIRED_STAMINA_TO_SPECIAL_ATTACK:
            damage_amount = int(self.damage * 2.5)
            self.stamina -= REQUIRED_STAMINA_TO_SPECIAL_ATTACK
            return f"{self.name} unleashes a powerful special attack!\n{target.take_damage(damage_amount)}"

        return f"{self.name} does not have enough stamina for a special attack."

    def heal(self):
        heal_amount = int(self.damage * 2)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        return f"{self.name} heals {heal_amount} HP and now has {self.hp} HP."

    def defend_attack(self):
        self.is_defending = True
        return f"{self.name} braces for impact and will reduce the next hit."