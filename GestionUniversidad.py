from enum import Enum
from abc import ABCMeta, abstractmethod

class Persona:
    def __init__(self,nombre,DNI,direccion,sexo):
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo
        
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
    def devuelve_datos(self):
        pass
      
class Asignatura:
    def __init__(self,nombre,id,creditos,horas):
        self.nombre  = nombre
        self.id = id
        self.creditos = creditos
        self.horas = horas
  
class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, asignaturas):
        Persona.__init__(self,nombre, DNI, direccion, sexo)
        self.asignaturas = asignaturas
    def devuelve_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo}')

class Investigador(Miembro_Departamento):
    def __init__(self,nombre,DNI,direccion,sexo,dep,area):
        Miembro_Departamento.__init__(self,nombre,DNI,direccion,sexo,dep)
        self.area = area
    def devuelve_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep}')
    
class Profesor_asociado(Miembro_Departamento):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas):
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, dep)
        self.asignaturas = asignaturas
    def devuelve_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep} Asignaturas: {self.asignaturas}')

class Profesor_titular(Investigador):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas,area):
        Investigador.__init__(self, nombre, DNI, direccion, sexo, dep, area)
        self.asignaturas = asignaturas
    def devuelve_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo} Departamento: {self.dep} Asignaturas: {self.asignaturas}')

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

    def devuelve_datos(self):
        print(f'Empleados: \n{[{i.nombre : i.DNI} for i in self.empleados]}')
        print(f'Estudiantes: \n{[{i.nombre : i.DNI} for i in self.estudiantes]}')

        
a1 = Asignatura('a', 123, 6, 36)
a2 = Asignatura('b', 456, 6, 42)
es1 = Estudiante('nombre3', '123456789A', 'direccion3', 'V', [a1, a2])
es2 = Estudiante('nombre4', '1245112346C', 'direccion4', 'V', [a1, a2])
dep = EDepartamento.DIIC
em1 = Profesor_asociado('nombre1', '31235213A', 'direccion', 'V', dep, [a1, a2])
em2 = Profesor_asociado('nombre2', '253156146B', 'direccion2', 'M', dep, [a1, a2])
u = Universidad([em1, em2], [es1, es2])

es3 = Estudiante('nombre5', '12451176534C', 'direccion5', 'M', [a1, a2])

u.devuelve_datos()
u.eliminar_estudiante(es2)
u.devuelve_datos()
