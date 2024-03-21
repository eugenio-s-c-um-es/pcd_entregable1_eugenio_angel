from enum import Enum
from abc import ABCMeta, abstractmethod

class Persona(metaclass = ABCMeta):
    def __init__(self,nombre,DNI,direccion,sexo):
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo
    
    @abstractmethod
    def muestra_datos(self):
        pass
    
    @abstractmethod
    def devuelve_datos(self):
        pass
        
class EDepartamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Miembro_Departamento(Persona,metaclass=ABCMeta):
    def __init__(self, nombre, DNI, direccion, sexo,dep):
        Persona.__init__(self,nombre, DNI, direccion, sexo)
        self.dep = dep
        
    def cambia_dep(self, dep):
        self.dep = dep
    
    @abstractmethod
    def muestra_datos(self):
        pass
    
    @abstractmethod
    def devuelve_datos(self):
        pass
      
class Asignatura:
    def __init__(self,nombre,id,creditos,horas):
        self.nombre  = nombre
        self.id = id
        self.creditos = creditos
        self.horas = horas
    def muestra_datos(self):
        print(f'Nombre:{self.nombre}, id: {self.id}, ETC: {self.creditos}, horas: {self.horas}')
    
    def devuelve_datos(self):
        return[self.nombre, self.id, self.creditos, self.horas]
  
class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, asignaturas):
        Persona.__init__(self,nombre, DNI, direccion, sexo)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo}')
        
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.asignaturas]

class Investigador(Miembro_Departamento):
    def __init__(self,nombre,DNI,direccion,sexo,dep,area):
        Miembro_Departamento.__init__(self,nombre,DNI,direccion,sexo,dep)
        self.area = area
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep}')
    
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.area]
    
class Profesor_asociado(Miembro_Departamento):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas):
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, dep)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep} Asignaturas: {self.asignaturas}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas]

class Profesor_titular(Investigador):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas,area):
        Investigador.__init__(self, nombre, DNI, direccion, sexo, dep, area)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep} Asignaturas: {self.asignaturas}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas, self.area]

class Universidad:
    def __init__(self,empleados,estudiantes):
        self.empleados = empleados
        self.estudiantes = estudiantes
        
    def anadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def anadir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)

    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def muestra_datos(self):
        print(f'Empleados: \n{[{i.nombre : i.DNI} for i in self.empleados]}')
        print(f'Estudiantes: \n{[{i.nombre : i.DNI} for i in self.estudiantes]}')
    
    def devuelve_datos(self):
        return[self.empleados, self.estudiantes]
