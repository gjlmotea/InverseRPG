print("... Include '", __package__, "' package: '" ,__name__, "'", sep="")

class Attr():
    def __init__(self, HP=1, MaxHP=1, Atk=1, Def=1, Dol=1):
        self.HP = HP
        self.MaxHP = MaxHP
        self.Atk = Atk
        self.Def = Def
        self.Dol = Dol

    def set_attr(self, attr, string):
        pass

    def set_HP(self, string):
        if isinstance(string, str) == False:
            raise TypeError("請輸入數值字串（需用引號括起）:", string)
        try:
            op = string[0]
            value = int(string[1:])
        except:
            raise Exception("請包含符號'+'或'-'或'='並輸入數值。Ex:'+123'、'-10'、'=50'...")
        if op == '=':
            self.HP = value
        elif op == '+':
            self.HP += value
        elif op == '-':
            self.HP -= value
        else:
            raise Exception("請包含符號'+'或'-'或'='。Ex:'+123'、'-10'、'=50'...")

            
    def split_op_and_value(self):
        pass
        
