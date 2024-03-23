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

class Miembro_Departamento(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, dep):
        super().__init__(nombre, DNI, direccion, sexo)
        self.dep = EDepartamento(dep)
        
    def cambia_dep(self, dep):
        self.dep = EDepartamento(dep)
    
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
        if not all(isinstance(item, str) for item in [nombre, DNI, direccion, sexo]):
            raise TypeError("El nombre, DNI, dirección y sexo deben ser strings")
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre} DNI: {self.DNI} Direccion: {self.direccion} Sexo: {self.sexo}')
        
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.asignaturas]

class Investigador(Miembro_Departamento):
    def __init__(self,nombre,DNI,direccion,sexo,dep,area):
        if not all(isinstance(item, str) for item in [nombre, DNI, direccion, sexo,area]):
            raise TypeError("El nombre, DNI, dirección, sexo y área deben ser strings")
        super().__init__(self,nombre,DNI,direccion,sexo,dep)
        self.area = area
        #self.asignaturas = None
        
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
     

    def dni_exists(self, dni, es_empleado):
        if es_empleado:
            return any(empleado.DNI == dni for empleado in self.empleados)
        else:
            return any(estudiante.DNI == dni for estudiante in self.estudiantes)
           
    def anadir_empleado(self, empleado):
        if self.dni_exists(empleado.DNI,1):
            raise ValueError("El DNI proporcionado ya se encuentra")
        self.empleados.append(empleado)


    def anadir_estudiante(self, estudiante):
        if self.dni_exists(estudiante.DNI,0):
            raise ValueError("El DNI proporcionado ya se encuentra")
        self.estudiantes.append(estudiante)

    def eliminar_empleado(self, DNI):
        for i in self.empleados:
            if i.DNI == DNI:
                self.empleados.remove(i)
                return
        raise ValueError("No se encuentra el DNI en la BD")

    def eliminar_estudiante(self, DNI):
        for i in self.estudiantes:
            if i.DNI == DNI:
                self.estudiantes.remove(i)
                return
        raise ValueError("No se encuentra el DNI en la BD")
    
    def muestra_datos(self):
        print(f'Empleados: \n{[{i.nombre : i.DNI} for i in self.empleados]}')
        print(f'Estudiantes: \n{[{i.nombre : i.DNI} for i in self.estudiantes]}')
    
    def devuelve_datos(self):
        return[self.empleados, self.estudiantes]
    
    def cambia_dep(self,empleado,dep):
        empleado.cambia_dep(dep)

    def mostrar_investigadores(self):
        for empleado in self.empleados:
            if isinstance(empleado, Investigador):
                empleado.muestra_datos()

    def mostrar_profesores_titulares(self):
        for empleado in self.empleados:
            if isinstance(empleado, Profesor_titular):
                empleado.muestra_datos()
    def mostrar_profesores_asociados(self):
        for empleado in self.empleados:
            if isinstance(empleado, Profesor_asociado):
                empleado.muestra_datos()