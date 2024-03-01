class Cuarto:
    "numVentanas, medida"

    def __init__(self, numVentanas, medidas):
        self.__numVentanas=numVentanas
        self.__medidas=medidas

    def getNumVentanas(self):
        return self.__numVentanas

    def getMedidas(self):
        return  self.__medidas

    def setNumVentanas(self, numVentanas):
        self.__numVentanas=numVentanas

    def setMedidas(self,medidas):
        self.__medidas=medidas

    class Patio:
        "Area social, medidas, descripcion"
        def __init__(self, areaSocial,medidas, descripcion):
            self.__areaSocial=areaSocial
            self.__medidas=medidas
            self.__descripcion=descripcion

        def getAreaSocial(self):
            return self.__areaSocial

        def getMedidas(self):
            return self.__medidas

        def getDescripcion(self):
            return self.__descripcion

        def setAreaSocial(self,areaSocial):
            self.__areaSocial= areaSocial

        def setMedidas(self,medidas):
            self.__medidas=medidas

        def setDescripcion(self, descripcion):
            self.__descripcion=descripcion


    class Sala:
        "chimenea, descripcion"

        def __init__(self, chimenea, descripcion):
            self.__chimenea=chimenea
            self.__descripcion=descripcion


        def getChimenea(self):
            return self.__chimenea

        def getDescripcion(self):
            return self.__descripcion

        def setChimenea(self,chimenea):
            self.__chimenea=chimenea

        def setDescripcion(self,descripcion):
            self.__descripcion=descripcion

    class LavaTrastos:
        "depositos, aguacaliente"

        def __init__(self, depositos,aguacaliente):
            self.__depositos=depositos
            self.__aguacaliente=aguacaliente

        def getDepositos(self):
            return self.__depositos

        def detAguaCaliente(self):
            return self.__aguacaliente

        def setDepositos(self,depositos):
            self.__depositos=depositos

        def setAguaCaliente(self,aguacaliente):
            self.__aguacaliente=aguacaliente

    class Estado:
        "nombre, fecha"
        def __init__(self, nombre, fecha):
            self.__nombre=nombre
            self.__fecha=fecha


    class Cocina:
        "electrodomes, medidas, material "

        def __init__(self, electrodomes,medidas, material,lavatrastos):
            self.__electradomes=electrodomes
            self.__medidas=medidas
            self.__material=material
            self
