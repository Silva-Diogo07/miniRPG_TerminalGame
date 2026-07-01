from .character import Character

import random

class Enemy(Character):
    enemy_types = [
        ("Goblin", 20, 5, "knife", 28, 3),
        ("Skeleton", 75, 15, "sword", 8, 1),
        ("Dragon", 300, 75, "fire", 20, 5),
        ("Capybara", 50, 1, "spit", 12, 8),
    ]

    def __init__(self, name, hp, damage, weapon, agility, stamina):
        super().__init__(name, hp, damage, weapon, agility, stamina)
        self.base_agility = agility
        self.base_stamina = stamina

    @classmethod
    def create_random_enemy(cls):
        enemy_data = random.choice(cls.enemy_types)
        return cls(*enemy_data)