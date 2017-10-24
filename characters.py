from Classes.abilities import *
# Making a standard character class for the player and enemies


class Person:

    def __init__(self, name, hp, atk, sta, exp, lvl, abilities):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atkh = atk + 5
        self.atkl = atk - 5
        self.max_sta = sta
        self.sta = sta
        self.exp = exp
        self.lvl = lvl
        self.lvl_exp = lvl * 20
        self.abilities = abilities
        self.actions = ["Basic Attack", "Abilities"]

    # Function to generate damage
    def deal_dmg(self):
        return random.randint(self.atkl, self.atkh)

    def increase_xp_cap(self, lvl):
        return lvl * 20

    # Function that allows our player and enemies to take damage
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # Lets us get our current hit points
    def get_hp(self):
        return self.hp

    # Lets us get our current stamina
    def get_sta(self):
        return self.sta

    # Lets us decrease our stamina based on the cost of our ability used
    def reduce_sta(self, cost):
        self.sta -= cost
        if self.sta < 0:
            self.sta = 0
        return self.sta

    # Lets us choose an action, whether a basic attack or ability
    def choose_action(self):
        i = 1
        print("\nChoose your action:\n")
        for item in self.actions:
            print("{}: {}".format([i], item))
            i += 1

    # If we choose to use an ability lets us choose which one
    def choose_ability(self):
        i = 1
        print("\nChoose your ability:\n")
        for ability in self.abilities:
            print("{}:{} (cost: {})".format([i], ability.name, ability.cost))
            i += 1

    # Levels up our player stats if exp requirement is met post battle
    def level_up(self):
        print("You leveled up!")
        self.lvl += 1
        self.max_hp += 10
        self.atkl += 10
        self.atkh += 10
        self.exp -= self.lvl_exp
        self.lvl_exp = (self.increase_xp_cap(self.lvl))

    # Player gains exp based off the enemy, then checks to see
    # whether the requirement for levelling up has been met
    def exp_gain(self, exp):
        self.exp += exp
        if self.exp >= self.lvl_exp:
            self.level_up()

    def recover(self):
        self.hp = self.max_hp
        self.sta = self.max_sta


# Creating Player Abilities
punch = Ability("Punch", 20, 5, "Punch them!")
strike = Ability("Lightning Strike", 30, 10, "black")
thrash = Ability("Thrash", 50, 18, "black")
slam = Ability("Slam", 65, 22, "black")

# List containing our abilities
player_abilities = [punch, strike, thrash, slam]

# This is our players character
player = Person("Chris", 300, 10, 100, 0, 1, player_abilities)

# Easiest enemies we'll face
# Just something to remember which slot is for which variables
#                     HP  AT  ST  XP LV  AC
wolf = Person("Wolf", 50, 15, 20, 3, 1, [])
bear = Person("Bear", 75, 20, 20, 5, 1, [])
bandit = Person("Bandit", 60, 25, 20, 5, 1, [])
witch = Person("Witch", 100, 30, 20, 6, 1, [])

# List with beginning enemies
beg_enemies = [wolf, bear, bandit, witch]

# Some more difficult mid range enemies, all numbers will be balanced later
centaur = Person("Centaur", 200, 40, 20, 10, 3, [])
goblin = Person("Goblin", 175, 40, 20, 10, 3, [])
chimera = Person("Chimera", 175, 35, 20, 10, 3, [])

# List of mid range enemies
mid_enemies = [centaur, goblin, chimera]

# Highest level enemies at the moment
dragon = Person("Dragon", 400, 90, 20, 20, 6, [])
thunderbird = Person("Thunder Bird", 400, 90, 20, 20, 6, [])
golem = Person("Golem", 450, 80, 20, 20, 6, [])

# List of Hardest enemies
hard_enemies = [dragon, thunderbird, golem]
