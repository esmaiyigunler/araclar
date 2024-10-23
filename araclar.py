class TemelArac:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def bilgi(self):
        print(f"marka: {self.marka}, Model:{self.model}")
class ElektrikliArac(TemelArac):
    def __init__(self,marka,model,batarya):
        super().__init__(marka,model)
        self.batarya=batarya
    def bilgi(self):
        super().bilgi()
        print(f"Batarya:{self.batarya}")
class LuksArac(TemelArac):
    def __init__(self,marka,model,konfor):
        super().__init__(marka,model)
        self.konfor=konfor
    def bilgi(self):
        super().bilgi()
        print(f"konfor: {self.konfor}")
araba1=TemelArac("porsche","12334")
araba2=ElektrikliArac("bmw","2222",100)
araba3=LuksArac("audi","98989","konforlu")
araba1.bilgi()
araba2.bilgi()
araba3.bilgi()
        
        
        
