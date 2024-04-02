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
    def __init__(self, nombre, id, creditos, horas):
        if not all(isinstance(item, str) for item in [nombre, id]):
            raise TypeError("El nombre y el ID deben ser strings")
        if not isinstance(creditos, int):
            raise TypeError("Los créditos deben ser un entero")
        if not isinstance(horas, int):
            raise TypeError("Las horas deben ser un entero")
        
        self.nombre = nombre
        self.id = id
        self.creditos = creditos
        self.horas = horas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, ID: {self.id}, Créditos: {self.creditos}, Horas: {self.horas}')
    
    def devuelve_datos(self):
        return [self.nombre, self.id, self.creditos, self.horas]
    
    
  
class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, asignaturas):
        if not all(isinstance(item, str) for item in [nombre, DNI, direccion, sexo]):
            raise TypeError("El nombre, DNI, dirección y sexo deben ser strings")
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}, Sexo: {self.sexo}')
        
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.asignaturas]

class Investigador(Miembro_Departamento):
    def __init__(self,nombre,DNI,direccion,sexo,dep,area):
        if dep not in EDepartamento.__members__:
            raise ValueError("El departamento debe ser uno de los valores del enum EDepartamento")
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, EDepartamento[dep])
        
        if not all(isinstance(item, str) for item in [nombre, DNI, direccion, sexo,area]):
            raise TypeError("El nombre, DNI, dirección, sexo y área deben ser strings")
        self.area = area
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.dep.name}')
    
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.area]
    
class Profesor_asociado(Miembro_Departamento):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas):
        if dep not in EDepartamento.__members__:
            raise ValueError("El departamento debe ser uno de los valores del enum EDepartamento")
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, EDepartamento[dep])
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.dep.name}, Asignaturas: {self.asignaturas}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas]

class Profesor_titular(Investigador):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas,area):
        if dep not in EDepartamento.__members__:
            raise ValueError("El departamento debe ser uno de los valores del enum EDepartamento")
        Investigador.__init__(self, nombre, DNI, direccion, sexo, dep, area)
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.dep.name}, Asignaturas: {self.asignaturas}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas, self.area]

class Universidad:
    def __init__(self,empleados,estudiantes,asginaturas):
        if not all(isinstance(empleado, Miembro_Departamento) for empleado in empleados):
            raise TypeError("Todos los empleados deben ser instancias de la clase Miembro_Departamento")
        if not all(isinstance(estudiante, Estudiante) for estudiante in estudiantes):
            raise TypeError("Todos los estudiantes deben ser instancias de la clase Estudiante")
        self.empleados = empleados
        self.estudiantes = estudiantes
        self.asignaturas = asginaturas
        
    def anadir_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise TypeError("La asignatura debe ser una instancia de la clase Asignatura")
        self.asignaturas.append(asignatura)
        
    def eliminar_asignatura(self, id):
        for asignatura in self.asignaturas:
            if asignatura.id == id:
                self.asignaturas.remove(asignatura)
                return
        raise ValueError("No se encuentra el ID en la BD")

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
                
    def mostrar_asignaturas(self):
        asignaturas_ordenadas = sorted(self.asignaturas, key=lambda x: x.id)
        for asignatura in asignaturas_ordenadas:
            print(f'ID: {asignatura.id}, Nombre: {asignatura.nombre}')


def menu():
    u = Universidad([], [], [])  # inicializa la universidad con listas vacías de empleados y estudiantes y asignaturas

    while True:
        print("\nMenu:"
              "\n1. Añadir profesor titular"
              "\n2. Añadir profesor asociado"
              "\n3. Añadir investigador"
              "\n4. Añadir estudiante"
              "\n5. Eliminar empleado"
              "\n6. Eliminar estudiante"
              "\n7. Mostrar profesores titulares"
              "\n8. Mostrar profesores asociados"
              "\n9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            # añadir profesor titular
            nombre = input("Nombre: ")
            DNI = input("DNI: ")
            direccion = input("Dirección: ")
            sexo = input("Sexo: ")
            dep = input("Departamento (DIIC, DITEC, DIS): ")
            area = input("Área de investigación: ")
            asignaturas = []

            while True:
                opcion = input("¿Desea añadir una asignatura? (s/n): ")
                if opcion.lower() == 's':
                    u.mostrar_asignaturas()
                    id_asignatura = input("ID de la asignatura: ")
                    try:
                        id_asignatura = int(id_asignatura)
                    except ValueError:
                        print("El ID de la asignatura debe ser un número entero.")
                        continue
                    asignaturas.append(id_asignatura)
                elif opcion.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Por favor, elige 's' o 'n'.")

            profesor_titular = Profesor_titular(nombre, DNI, direccion, sexo, dep, asignaturas, area)
            u.anadir_empleado(profesor_titular) 
            print("Profesor titular añadido correctamente.")
        
        elif opcion == '2':
            # añadir profesor asociado
            nombre = input("Introduce el nombre del profesor asociado: ")
            DNI = input("Introduce el DNI del profesor asociado: ")
            direccion = input("Introduce la dirección del profesor asociado: ")
            sexo = input("Introduce el sexo del profesor asociado (V/M): ")
            dep = input("Introduce el departamento del profesor asociado (DIIC/DITEC/DIS): ")

            asignaturas = []
            while True:
                print("¿Quieres añadir una asignatura al profesor asociado? (s/n)")
                opcion = input()
                if opcion.lower() == 's':
                    id_asignatura = input("Introduce el ID de la asignatura: ")
                    try:
                        id_asignatura = int(id_asignatura)
                    except ValueError:
                        print("El ID de la asignatura debe ser un número entero.")
                        continue
                    asignaturas.append(id_asignatura)
                elif opcion.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Por favor, elige 's' o 'n'.")

            profesor_asociado = Profesor_asociado(nombre, DNI, direccion, sexo, dep, asignaturas)
            u.anadir_empleado(profesor_asociado)
            print("Profesor asociado añadido correctamente.")
            
        elif opcion == '3':
            
            nombre = input("Introduce el nombre del investigador: ")
            DNI = input("Introduce el DNI del investigador: ")
            direccion = input("Introduce la dirección del investigador: ")
            sexo = input("Introduce el sexo del investigador (V/M): ")
            dep = input("Introduce el departamento del investigador (DIIC/DITEC/DIS): ")
            area = input("Introduce el área de investigación del investigador: ")

            investigador = Investigador(nombre, DNI, direccion, sexo, dep, area)
            u.anadir_empleado(investigador)
            print("Investigador añadido correctamente.")
            
            
        elif opcion == '4':
            # añadir estudiante
            nombre = input("Introduce el nombre del estudiante: ")
            DNI = input("Introduce el DNI del estudiante: ")
            direccion = input("Introduce la dirección del estudiante: ")
            sexo = input("Introduce el sexo del estudiante (V/M): ")

            asignaturas = []
            while True:
                print("¿Quieres añadir una asignatura al estudiante? (s/n)")
                opcion = input()
                if opcion.lower() == 's':
                    id_asignatura = input("Introduce el ID de la asignatura: ")
                    try:
                        id_asignatura = int(id_asignatura)
                    except ValueError:
                        print("El ID de la asignatura debe ser un número entero.")
                        continue
                    asignaturas.append(id_asignatura)
                elif opcion.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Por favor, elige 's' o 'n'.")

            estudiante = Estudiante(nombre, DNI, direccion, sexo, asignaturas)
            u.anadir_estudiante(estudiante)
            print("Estudiante añadido correctamente.")
            
        elif opcion == '5':
            DNI = input("Introduce el DNI del empleado a eliminar: ")
            u.eliminar_empleado(DNI)
            print("Empleado eliminado correctamente.")
        elif opcion == '6':
            DNI = input("Introduce el DNI del estudiante a eliminar: ")
            u.eliminar_estudiante(DNI)
            print("Estudiante eliminado correctamente.")
        elif opcion == '7':
            u.mostrar_profesores_titulares()
        elif opcion == '8':
            u.mostrar_profesores_asociados()
        elif opcion == '9':
            break  # salir del bucle
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 9.")

if __name__ == "__main__":
    menu()