from core import battle
from obj import monster
from obj import attr
from os import getcwd

if __name__ == '__main__':
    print("This is '", __package__, "' package: '" ,__name__, "'", sep="")
    base_path = getcwd()
    print(base_path)

a = attr.Attr()
print(a.HP, a.MaxHP, a.Atk, a.Def)
ll = [1,2,3,4]

a.set_HP("=123")
print(a.HP, a.MaxHP, a.Atk, a.Def)

#a.set_attr("HP", "=123")
