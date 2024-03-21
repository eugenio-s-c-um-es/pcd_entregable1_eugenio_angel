from GestionUniversidad import *
import pytest


if __name__ == '__main__':

    a1 = Asignatura('a', 123, 6, 36)
    a2 = Asignatura('b', 456, 6, 42)
    es1 = Estudiante('nombre3', '123456789A', 'direccion3', 'V', [a1, a2])
    es2 = Estudiante('nombre4', '1245112346C', 'direccion4', 'V', [a1, a2])
    dep = EDepartamento.DIIC
    em1 = Profesor_asociado('nombre1', '31235213A', 'direccion', 'V', dep, [a1, a2])
    em2 = Profesor_asociado('nombre2', '253156146B', 'direccion2', 'M', dep, [a1, a2])
    u = Universidad([em1, em2], [es1])

    es3 = Estudiante('nombre5', '12451176534C', 'direccion5', 'M', [a1, a2])

    u.muestra_datos()
    u.anadir_estudiante(es2)
    u.eliminar_estudiante('123456789A')
    u.muestra_datos()
    a2.muestra_datos()
    print(a2.devuelve_datos())
