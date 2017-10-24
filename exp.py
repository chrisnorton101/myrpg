class Player:
    def __init__(self, name, hp, atk, exp, max_exp, lvl):
        self.hp = hp
        self.atk = atk
        self.name = name
        self.exp = exp
        self.max_exp = max_exp
        self.lvl = lvl

    def level_up(self):
        print("You levelled up!")
        self.lvl += 1
        self.hp += 10
        self.atk += 10
        self.exp -= self.max_exp

    def exp_gain(self, exp):
        self.exp += exp
        if self.exp >= self.max_exp:
            self.level_up()


chris = Player("Chris", 10, 10, 0, 20, 1)
chris.exp_gain(25)
print(chris.exp, chris.atk, chris.hp, chris.lvl)
