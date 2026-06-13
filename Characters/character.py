class Character:
    def __init__(self, name, hp, damage, weapon):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon = weapon


    def take_damage(self, amount):

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0
            return f"{self.name} died"

        return f"{self.name} has {self.hp} HP left"
    
    def attack(self, target):
        return target.take_damage(self.damage)