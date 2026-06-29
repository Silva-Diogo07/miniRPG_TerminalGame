import random

class Character:
    def __init__(self, name, hp, damage, weapon, agility):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon = weapon
        self.agility = agility

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage_amount):
        self.hp -= damage_amount

        if self.hp <= 0:
            self.hp = 0
            return f"{self.name} died"

        return f"{self.name} has {self.hp} HP left"
    
    def dodged(self):
        # if number <= agility , then attacked was dodge , else attack not dodge
        return random.randint(1, 100) <= self.agility
    

    def attack(self, target):
        if target.dodged():
            return f"{target.name} dodged {self.name}'s attack"
        
        print(f"{self.name} dealt {self.damage} damage to {target.name}")
        return target.take_damage(self.damage)