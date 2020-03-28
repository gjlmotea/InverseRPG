print("... Include '", __package__, "' package: '" ,__name__, "'", sep="")

class Attr():
    def __init__(self, HP=1, MaxHP=1, Atk=1, Def=1, Dol=1):
        self.HP = HP
        self.MaxHP = MaxHP
        self.Atk = Atk
        self.Def = Def
        self.Dol = Dol

    def set_attr(self, attr, string):
        self.dict = {
            'HP':self.HP,
            'MaxHP':self.MaxHP,
            'Atk':self.Atk,
            'Def':self.Def,
            'Dol':self.Dol,
        }
        try:
            self.attr = self.dict[attr]
        except:
            raise Exception("沒有'"+ attr+ "'這個屬性")
        
        if isinstance(string, str) == False:
            raise TypeError("請輸入數值字串（需用引號括起）:", string)
        try:
            op = string[0]
            value = int(string[1:])
        except:
            raise Exception("請包含符號'+'或'-'或'='並輸入數值。Ex:'+123'、'-10'、'=50'...")

        if op == '=':
            self.attr = value
        elif op == '+':
            self.attr += value
        elif op == '-':
            self.attr -= value
        else:
            raise Exception("請包含符號'+'或'-'或'='。Ex:'+123'、'-10'、'=50'...")
        print("幹", self.dict[attr])
        self.dict[attr] = self.attr
        print(",,,,,,",self.dict[attr])
##        if attr == "HP":
##            self.HP = self.attr
##        elif attr == "MaxHP":
##            self.attr = self.MaxHP
        
        print("現在血量",self.HP)


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
        
