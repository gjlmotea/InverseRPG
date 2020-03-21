from core import battle
from object import monster
from object import player
from os import getcwd

if __name__ == '__main__':
    print("This is '", __package__, "' package: '" ,__name__, "'", sep="")
    base_path = getcwd()
    print(base_path)

a = player.player(1000)
print(a.HP)
