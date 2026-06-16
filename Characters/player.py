from .character import Character

class Player(Character):
    def __init__(self, name, hp, damage, weapon, dodge):
        super().__init__(name, hp, damage, weapon, dodge)
        self.base_dodge = dodge

    def focus(self):
        self.dodge += 10

    def reset_dodge_chance(self):
        self.dodge = self.base_dodge