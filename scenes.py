from Classes.characters import *
# Creating an intro scene


def intro():
    print("""Welcome to the game! In this game you
will battle against enemies in dungeons and across
the lands. As you battle you will level up and get
in order to face tougher enemies. Your ultimate goal
is to become the Leader of the lands!\n\n""")


def cave():
    print("You enter a cave and hear a noise in the distance.")
    print("As you walk deeper into the cave you feel a chill in the air.")
    print("It's too late to turn back now, the noise has led you deeper")
    print("into the cave unwillingly. You turn the corner and are face to")
    print("face with your worst fear.")


def home():
    print("You return home in hopes of some rest and relaxation.")
    print("Before you can take your boots off you collapse onto your bed")
    print("from exhaustion. You drift off into the comfort of your dreams.")
    player.recover()
    print("HP: {}".format(player.hp))
    print("Stamina: {}".format(player.sta))
    print("Level: {}".format(player.lvl))
