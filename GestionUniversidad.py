from enum import Enum
from abc import ABCMeta, abstractmethod

class Persona(metaclass = ABCMeta):
    def __init__(self,nombre,DNI,direccion,sexo):
        if not all(isinstance(item, str) for item in [nombre, DNI, direccion]):
            raise TypeError("El nombre, DNI, dirección deben ser strings")
        if sexo not in ['V', 'M']:
            raise ValueError("El sexo debe ser 'V' o 'M'")
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
        if dep not in EDepartamento.__members__:
            raise ValueError("El departamento debe ser uno de los valores del enum EDepartamento")
        super().__init__(nombre, DNI, direccion, sexo)
        self.dep = EDepartamento[dep]
        
    def cambia_dep(self, dep):
        self.dep = EDepartamento[dep]
    
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
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        super().__init__(nombre, DNI, direccion, sexo)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}')
        
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.asignaturas]

class Investigador(Miembro_Departamento):
    def __init__(self,nombre,DNI,direccion,sexo,dep,area):
        if not isinstance(area, str):
            raise TypeError("El área debe ser un string")
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, EDepartamento[dep])
        self.area = area
        
    def muestra_datos(self):
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Direccion: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.dep.name}')
    
    def devuelve_datos(self):
        return [self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.area]
    
class Profesor_asociado(Miembro_Departamento):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas):
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        
        Miembro_Departamento.__init__(self,nombre, DNI, direccion, sexo, EDepartamento[dep])
    
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        asignaturas = [asignatura.nombre for asignatura in self.asignaturas]
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Departamento: {self.dep.name}, Asignaturas: {asignaturas}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas]

class Profesor_titular(Investigador):
    def __init__(self, nombre, DNI, direccion, sexo, dep, asignaturas, area):
        if not all(isinstance(asignatura, Asignatura) for asignatura in asignaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
        Investigador.__init__(self, nombre, DNI, direccion, sexo, dep, area)
        self.asignaturas = asignaturas
        
    def muestra_datos(self):
        asignaturas = [asignatura.nombre for asignatura in self.asignaturas]
        print(f'Nombre: {self.nombre}, DNI: {self.DNI}, Departamento: {self.dep.name}, Asignaturas: {asignaturas}, Área: {self.area}')

    def devuelve_datos(self):
        return[self.nombre, self.DNI, self.direccion, self.sexo, self.dep, self.asignaturas, self.area]

class Universidad:
    def __init__(self,empleados,estudiantes,asginaturas):
        if not all(isinstance(empleado, Miembro_Departamento) for empleado in empleados):
            raise TypeError("Todos los empleados deben ser instancias de la clase Miembro_Departamento")
        if not all(isinstance(estudiante, Estudiante) for estudiante in estudiantes):
            raise TypeError("Todos los estudiantes deben ser instancias de la clase Estudiante")
        if not all(isinstance(asignatura, Asignatura) for asignatura in asginaturas):
            raise TypeError("Todas las asignaturas deben ser instancias de la clase Asignatura")
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
    
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            estudiante.muestra_datos()


def menu():
    u = Universidad([], [], [])  # inicializa la universidad con listas vacías de empleados y estudiantes y asignaturas

    while True:
        print("\nMenu:"
              "\n1. Añadir profesor titular"
              "\n2. Añadir profesor asociado"
              "\n3. Añadir investigador"
              "\n4. Añadir estudiante"
              "\n5. Añadir asignatura"
              "\n6. Eliminar empleado"
              "\n7. Eliminar estudiante"
              "\n8. Eliminar asignatura"
              "\n9. Mostrar profesores titulares"
              "\n10. Mostrar profesores asociados"
              "\n11. Mostrar asignaturas"
              "\n12. Mostrar investigadores"
              "\n13. Mostrar estudiantes"
              "\n14. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            # añadir profesor titular
            nombre = input("Introduce el nombre del profesor titular: ")
            DNI = input("Introduce el DNI del profesor titular: ")
            direccion = input("Introduce la dirección del profesor titular: ")
            sexo = input("Introduce el sexo del profesor titular (V/M): ")
            dep = input("Introduce el departamento del profesor titular (DIIC/DITEC/DIS): ")
            area = input("Introduce el área de investigación del profesor titular: ")
            asignaturas = []

            while True:
                opcion = input("¿Desea añadir una asignatura? (s/n): ")
                if opcion.lower() == 's':
                    print("Asignaturas disponibles:")
                    u.mostrar_asignaturas()
                    id_asignatura = input("ID de la asignatura: ")
                    aux = True
                    for asignatura in u.asignaturas:
                        if id_asignatura == asignatura.id:
                            asignaturas.append(Asignatura(asignatura.nombre, asignatura.id, asignatura.creditos, asignatura.horas))
                            print("Asignatura añadida correctamente.")
                            aux = False
                    if aux:
                        print("El ID de la asignatura debe coincidir con uno de los disponibles.")
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
                    print("Asignaturas disponibles:")
                    u.mostrar_asignaturas()
                    id_asignatura = input("ID de la asignatura: ")
                    aux = True
                    for asignatura in u.asignaturas:
                        if id_asignatura == asignatura.id:
                            asignaturas.append(Asignatura(asignatura.nombre, asignatura.id, asignatura.creditos, asignatura.horas))
                            print("Asignatura añadida correctamente.")
                            aux = False
                    if aux:
                        print("El ID de la asignatura debe coincidir con uno de los disponibles.")
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
                    print("Asignaturas disponibles:")
                    u.mostrar_asignaturas()
                    id_asignatura = input("ID de la asignatura: ")
                    aux = True
                    for asignatura in u.asignaturas:
                        if id_asignatura == asignatura.id:
                            asignaturas.append(Asignatura(asignatura.nombre, asignatura.id, asignatura.creditos, asignatura.horas))
                            print("Asignatura añadida correctamente.")
                            aux = False
                    if aux:
                        print("El ID de la asignatura debe coincidir con uno de los disponibles.")
                elif opcion.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Por favor, elige 's' o 'n'.")

            estudiante = Estudiante(nombre, DNI, direccion, sexo, asignaturas)
            u.anadir_estudiante(estudiante)
            print("Estudiante añadido correctamente.")
        elif opcion == '5':
            # Añadir asignatura
            nombre = input("Introduce el nombre de la asignatura: ")
            id = input("Introduce el ID de la asignatura: ")
            creditos = int(input("Introduce los créditos de la asignatura: "))
            horas = int(input("Introduce las horas de la asignatura: "))
            asignatura = Asignatura(nombre, id, creditos, horas)
            u.anadir_asignatura(asignatura)
            print("Asignatura añadida correctamente.")
        elif opcion == '6':
            DNI = input("Introduce el DNI del empleado a eliminar: ")
            u.eliminar_empleado(DNI)
            print("Empleado eliminado correctamente.")
        elif opcion == '7':
            DNI = input("Introduce el DNI del estudiante a eliminar: ")
            u.eliminar_estudiante(DNI)
            print("Estudiante eliminado correctamente.")
        elif opcion == '8':
            id = input("Introduce el ID de la asignatura a eliminar: ")
            u.eliminar_asignatura(id)
            print("Asignatura eliminada correctamente.")
        elif opcion == '9':
            u.mostrar_profesores_titulares()
        elif opcion == '10':
            u.mostrar_profesores_asociados()
        elif opcion == '11':
            u.mostrar_asignaturas()
        elif opcion == '12':
            u.mostrar_investigadores()
        elif opcion == '13':
            u.mostrar_estudiantes()
        elif opcion == '14':
            break  # salir del bucle
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 14.")

if __name__ == "__main__":
    menu()