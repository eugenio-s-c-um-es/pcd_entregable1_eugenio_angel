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
        
    def anadir_empleado(self, empleado, tipo):
        
        if not isinstance(empleado.nombre,str):
            raise TypeError("El nombre debe ser una string")
        if not isinstance(empleado.DNI,str):
            raise TypeError("El DNI debe ser una string")
        if not isinstance(empleado.direccion,str):
            raise TypeError("La dirección debe ser una string")
        if not isinstance(empleado.sexo,str):
            raise TypeError("El sexo debe ser una string")
        if not isinstance(empleado.dep,EDepartamento):
            raise TypeError("El departamento está mal")
        
        if tipo == 'asociado':
            for i in empleado.asignaturas:
                if not isinstance(i,Asignatura):
                    raise TypeError("La Asignatura está mal")
                    
        elif tipo == 'investigador':
            if not isinstance(empleado.area,str):
                raise TypeError("El área debe ser una string")
        else:
            if not isinstance(empleado.area,str):
                raise TypeError("El área debe ser una string")
            for i in empleado.asignaturas:
                if not isinstance(i,Asignatura):
                    raise TypeError("La Asignatura está mal")
            
        for i in self.empleados:
            if i.DNI == empleado.DNI:
                raise TypeError("El DNI proporcionado ya se encuentra")
        self.empleados.append(empleado)

    def anadir_estudiante(self, estudiante):
        
        if not isinstance(estudiante.nombre,str):
            raise TypeError("El nombre debe ser una string")
        if not isinstance(estudiante.DNI,str):
            raise TypeError("El DNI debe ser una string")
        if not isinstance(estudiante.direccion,str):
            raise TypeError("La dirección debe ser una string")
        if not isinstance(estudiante.sexo,str):
            raise TypeError("El sexo debe ser una string")
        for i in estudiante.asignaturas:
            if not isinstance(i,Asignatura):
                raise TypeError("La Asignatura está mal")
        for i in self.estudiantes:
            if i.DNI == estudiante.DNI:
                raise TypeError("El DNI proporcionado ya se encuentra")
        self.estudiantes.append(estudiante)

    def eliminar_empleado(self, DNI):
        for i in self.empleados:
            if i.DNI == DNI:
                self.empleados.remove(i)
                break
            raise TypeError("No se encuentra el DNI en la BD")
        

    def eliminar_estudiante(self, DNI):
        for i in self.estudiantes:
            if i.DNI == DNI:
                self.estudiantes.remove(i)
                break
            raise TypeError("No se encuentra el DNI en la BD")
    
    def muestra_datos(self):
        print(f'Empleados: \n{[{i.nombre : i.DNI} for i in self.empleados]}')
        print(f'Estudiantes: \n{[{i.nombre : i.DNI} for i in self.estudiantes]}')
    
    def devuelve_datos(self):
        return[self.empleados, self.estudiantes]
    
    def cambia_dep(self,empleado,dep):
        empleado.cambia_dep(dep)


#TODO def mostrar_investigadores()

#TODO def mostrar_profesores_titulares()

#TODO def mostrar_profesores_asociados()