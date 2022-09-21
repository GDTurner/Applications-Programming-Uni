import random


class Combat_func():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

        p_init = self.player.get_initiative()
        e_init = self.enemy.get_initiative()


        while self.enemy.alive():
            if p_init >= e_init and self.player.alive():
                self.player_attack()
                if self.enemy.alive():
                    self.npc_attack(self.enemy)
            elif e_init > p_init and self.enemy.alive():
                self.npc_attack(self.enemy)
                if self.player.alive():
                    self.player_attack()
            else:
                break

        self.player.timer = 0      

    def player_attack(self):
        if self.player.timer > 0:
            self.player.timer -= 1
        print("You're up.\nIt's time to fight. What do you want to do?")
        while True:
            print(f"1: Attack with - {self.player.weapon.name} | 2: {self.player.deck.ability_a} | 3: {self.player.deck.ability_b} | 4: Heal")
            c = ""
            c = input(">>> ")     
            if c == "1":
                self.player.attack_weapon(self.enemy)
                break
            elif c == "2":
                self.player.deck.abilityA(self.enemy, self.player)
                break
            elif c == "3":
                self.player.deck.abilityB(self.player)
                break
            elif c == "4":
                self.player.heal()
                break                
            else:
                print("That's not a valid input")  


    def npc_attack(self, npc):
        print(npc.weapon.attack_text())
        to_hit = random.randint(1,20) + (npc.weapon.accuracy + npc.dexterity)
        print(f"{npc.name} rolls {to_hit} to hit.")
        if to_hit >= self.player.stats.dexterity + 10:
            print(f"{npc.name} hits you!")
            damage = npc.weapon.damage + npc.strength
            self.player.hp -= damage
            if self.player.alive():
                print(f"{npc.name} deals {damage} damage to {self.player.name}. You have {self.player.hp} hp remaining.")
                return 
            else:
                print(f"{self.player.name} crumples to the ground, lifeless.")
                return 
        else:
            print(f"{npc.name} attack misses you.")
            return 


