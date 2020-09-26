class SerializerFactory:
    def get_serializer(many:bool):
        raise NotImplementedError("Metodo get_serializer no implementado")

class MensajeSerializerFactory(SerializerFactory):
        def get_serializer(many:bool):
            if(many): 
                return ListaMensajesSerializer()
            else:
                return MensajeIndSerializer()

class MensajeSerializer:
    campos = ["id","texto","room","estado"]
    
    def data(msg):
        raise NotImplementedError("Método data no implementado")


class MensajeIndSerializer(MensajeSerializer):
    def data(self,msg):
        dic = {}
        for c in self.campos:
            dic[c] = getattr(msg,c)
        return dic

class ListaMensajesSerializer(MensajeSerializer):
    def data(self,msg):
        lista = []
        for m in msg:
            dic = {}
            for c in self.campos:
                dic[c] = getattr(m,c)
            lista.append(dic)
        
        return lista


