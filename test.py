from core import battle
from object import monster
from object import player
from os import getcwd

if __name__ == '__main__':
    print("This is '", __package__, "' package: '" ,__name__, "'", sep="")
    base_path = getcwd()
    print(base_path)

a = player.Attr()
a.default_attr
print(a.HP, a.MaxHP, a.Atk, a.Def)
a.set_HP("=", 123.59)
print(a.HP, a.MaxHP, a.Atk, a.Def)

