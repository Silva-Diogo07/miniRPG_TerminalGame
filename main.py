from Characters.character import Character

player = Character("Player", 100, 200, "Melee")
enemy = Character("Enemy", 75, 20, "Axe")

while player.hp > 0 and enemy.hp > 0:

    print(f"{player.name} attacked {enemy.name}")
    player.attack(enemy)

    if enemy.hp > 0:
        print(f"{enemy.name} attacked {player.name}")
        enemy.attack(player)  


if player.hp <= 0:
    print("Player died")
else:
    print("Enemy died")