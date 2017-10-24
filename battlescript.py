from Classes.characters import *
from Classes.abilities import *
import time


player = player
enemy = beg_enemies[random.randrange(0,4)]


def battle():
    print("A {} has attacked!".format(enemy.name))
    time.sleep(1)
    running = True
    while running:
        print("==================")
        player.choose_action()
        choice = int(input("\nAction: ")) - 1

        if choice == 0:
            dmg = player.deal_dmg()
            enemy.take_dmg(dmg)
            print("\nYou attacked for {} points of damage!".format(dmg))
            time.sleep(1)

        elif choice == 1:
            player.choose_ability()
            ability_choice = int(input("Ability: ")) - 1

            ability = player.abilities[ability_choice]

            ability_dmg = ability.generate_dmg()

            current_sta = player.get_sta()

            if ability.cost > current_sta:
                print("You don't have enough stamina!")
                continue

            player.reduce_sta(ability.cost)

            enemy.take_dmg(ability_dmg)

            print("\n{} deals {} points of damage!".format(ability.name, ability_dmg))
            time.sleep(1)

        else:
            print("\nMake a proper selection!")
            time.sleep(1)
            continue
            
        if enemy.get_hp() > 0:
            enemy_dmg = enemy.deal_dmg()
            player.take_dmg(enemy_dmg)

            print("\nThe Enemy Attacked for {} points of damage!".format(enemy_dmg))
            time.sleep(1)
            print("==================")
            print("Enemy HP: {}/{}".format(enemy.get_hp(), enemy.max_hp))
            print("{} HP: {}/{}".format(player.name, player.get_hp(), player.max_hp))
            print("Player Stamina: {}/{}".format(player.get_sta(), player.max_sta))
            time.sleep(1)

        elif enemy.get_hp() == 0:
            print("You have defeated the Enemy!")
            running = False
            player.exp_gain(enemy.exp)
            print("=================")
            print("You gained {} experience!".format(enemy.exp))
            print("Player Exp: {}/{}".format(player.exp, player.lvl_exp))
            print("Level {}".format(player.lvl))

        elif player.get_hp() == 0:
            print("You have been defeated!")
            running = False
