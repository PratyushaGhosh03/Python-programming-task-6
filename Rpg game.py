class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name} attacks {enemy.name}")
        enemy.take_damage(player.attack)
        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            break
        print(f"{enemy.name} attacks {player.name}")
        player.take_damage(enemy.attack)
    
    if player.is_alive():
        print("You won!")
    else:
        print("You lost!")

# Example usage
player = Character("Hero", 100, 20)
enemy = Character("Goblin", 50, 10)
battle(player, enemy)
