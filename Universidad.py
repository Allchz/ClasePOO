class Persona:
    def __init__(self, id, n1, n2, a1, a2, dir):
        self.__id = id
        self.__n1 = n1
        self.__n2 = n2
        self.__a1 = a1
        self.__a2 = a2
        self.__dir = dir

    def getId(self):
        return self.__id

    def getN1(self):
        return self.__n1

    def getN2(self):
        return self.__n2

    def getA1(self):
        return self.__a1

    def getA2(self):
        return self.__a2

    def getDir(self):
        return self.__dir

    def __str__(self):
        return f'{self.getId()} {self.getN1()} {self.getN2()} {self.getA1()} {self.getA2()} '


class Alumno(Persona):
    def __init__(self, id, n1, n2, a1, a2, dir, carrera, horario, ncuenta):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__carrera = carrera
        self.__horario = horario
        self.__ncuenta = ncuenta

    def getCarrera(self):
        return self.__carrera

    def getHorario(self):
        return self.__horario

    def getNcuenta(self):
        return self.__ncuenta

    def __str__(self):
        return super().__str__() + f'{self.__carrera} {self.getHorario()} {self.getNcuenta()} '


# alumno = Alumno('0801199900023', 'Cons', '', 'Sorto', 'Reyes', 'Tegucigalpa', 'IS', '7-9', '20222001212')
# print(alumno)

class Empleado(Persona):

    def __init__(self, id, n1, n2, a1, a2, dir, nEmp):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__nEmp = nEmp

    def getEmpleado(self):
        return self.__nEmp

    def __str__(self):
        return super().__str__() + f' {self.getEmpleado()} '


class Visitante(Persona):
    def __init__(self, id, n1, n2, a1, a2, dir, razon, edificio):
        super().__init__(id, n1, n2, a1, a2, dir)
        self.__razon = razon
        self.__edificio = edificio

    def getRazon(self):
        return self.__razon

    def getEdificio(self):
        return self.__edificio

    def __str__(self):
        return super().__str__() + f' {self.getRazon()} {self.getEdificio()} '


class Maestro(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion):
        Empleado.__init__(self, id, n1, n2, a1, a2, dir, nEmp)
        self.__facultad = facultad
        self.__especializacion = especializacion

    def getFacultad(self):
        return self.__facultad

    def getEspecializacion(self):
        return self.__especializacion

    def __str__(self):
        return super().__str__() + f' {self.getFacultad()}  {self.getEspecializacion()}'


class Administrativo(Empleado):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo):
        super().__init__(id, n1, n2, a1, a2, dir, nEmp)
        self.__area = area
        self.__campo = campo

    def getArea(self):
        return self.__area

    def getCampo(self):
        return self.__campo

    def __str__(self):
        return super().__str__() + f' {self.getArea()}  {self.getCampo()} '


class Jefe(Maestro, Administrativo):
    def __init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion, area, campo, fInicio, fFin):
        Maestro.__init__(self, id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion)
        Administrativo.__init__(self, id,n1,n2,a1, a2, dir, nEmp, area, campo)
        #super().__init__(id, n1, n2, a1, a2, dir, nEmp, facultad, especializacion)
        #Administrativo.__init__(self, id, n1, n2, a1, a2, dir, nEmp, area, campo)
        self.__finicio = fInicio
        self.__fFin = fFin

    def getFinicio(self):
        return self.__finicio

    def getFfin(self):
        return self.__fFin

    def __str__(self):
        return super().__str__() + f' {self.getFinicio()}  {self.getFfin()} '


jefe = Jefe(12, "Ariel", "Jose", "Perez", "Gomez", "su casa", 1232332, "Is", "Base de datos", "Ingenieria",
            "Base de datos", "20233/01/22", "2025/09/24")

print(jefe)
