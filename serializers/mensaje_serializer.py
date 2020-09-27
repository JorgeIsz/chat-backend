# Inspirado en gran medida de la clase ModelSerializer
# de la librería rest_framework de Django.

class MensajeSerializer:
    campos = ["id","texto","room","estado"]

    def __init__(self,msg,many):
        self.msg = msg

        if(many): 
            self.serializar_varios()
        else:
            self.serializar_uno()

    def serializar_uno(self):
        dic = {}
        for c in self.campos:
            dic[c] = getattr(self.msg,c)
        
        self.data = dic

    def serializar_varios(self):
        lista = []
        for m in self.msg:
            dic = {}
            for c in self.campos:
                dic[c] = getattr(m,c)
            lista.append(dic)
        
        self.data = lista

        

