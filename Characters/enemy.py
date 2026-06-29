from .character import Character

import random

class Enemy(Character):
    enemy_types = [
        ("Goblin", 20, 5, "knife", 28),
        ("Skeleton", 75, 15, "sword", 8),
        ("Dragon", 300, 75, "fire", 20),
        ("Capybara", 50, 1, "spit", 12),
    ]

    def __init__(self, name, hp, damage, weapon, agility):
        super().__init__(name, hp, damage, weapon, agility)
        self.base_agility = agility

    @classmethod
    def create_random_enemy(cls):
        enemy_data = random.choice(cls.enemy_types)
        return cls(*enemy_data)