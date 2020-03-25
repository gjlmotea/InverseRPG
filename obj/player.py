print("... Include '", __package__, "' package: '" ,__name__, "'", sep="")

class Attr():
    def __init__(self, HP=100, MaxHP=100, Atk=10, Def=10):
        self.HP = HP
        self.MaxHP = MaxHP
        self.Atk = Atk
        self.Def = Def

    def default_attr(self):
        self.HP = HP+1999
        self.MaxHP = MaxHP
        self.Atk = Atk
        self.Def = Def

    def set_HP(self, op='=', value=0):
        if isinstance(value, (int, float)) == False:
            raise TypeError('請輸入數字而非字串:', str(value))
        elif op == '=':
            self.HP = value
        elif op == '+':
            self.HP += value
        elif op == '-':
            self.HP -= value
        else:
            raise Exception("請輸入'+'或'-'或'=': '"+ op+ "'")

            
    def split_op_and_value(self):
        pass
        
