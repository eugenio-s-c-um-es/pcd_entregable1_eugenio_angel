import pytest
from GestionUniversidad import *

def test_añadir_profesor_titular():
    u = Universidad([], [], [])
    asignatura1 = Asignatura('a', 123, 6, 36)
    asignatura2 = Asignatura('b', 456, 6, 42)
    u.anadir_asignatura(asignatura1)
    u.anadir_asignatura(asignatura2)
    profesor_titular = Profesor_titular('nombre', '123456789A', 'direccion', 'V', EDepartamento.DIIC, [123, 456], 'area')
    u.anadir_empleado(profesor_titular)
    assert profesor_titular in u.empleados

def test_añadir_profesor_asociado():
    u = Universidad([], [], [])
    asignatura1 = Asignatura('a', 123, 6, 36)
    asignatura2 = Asignatura('b', 456, 6, 42)
    u.anadir_asignatura(asignatura1)
    u.anadir_asignatura(asignatura2)
    profesor_asociado = Profesor_asociado('nombre', '123456789A', 'direccion', 'V', EDepartamento.DIIC, [123, 456])
    u.anadir_empleado(profesor_asociado)
    assert profesor_asociado in u.empleados

def test_añadir_estudiante():
    u = Universidad([], [])
    asignatura1 = Asignatura('a', 123, 6, 36)
    asignatura2 = Asignatura('b', 456, 6, 42)
    u.anadir_asignatura(asignatura1)
    u.anadir_asignatura(asignatura2)
    estudiante = Estudiante('nombre', '123456789A', 'direccion', 'V', [123, 456])
    u.anadir_estudiante(estudiante)
    assert estudiante in u.estudiantes

def test_añadir_asignatura():
    u = Universidad([], [])
    asignatura = Asignatura('a', 123, 6, 36)
    u.anadir_asignatura(asignatura)
    assert asignatura in u.asignaturas

def test_eliminar_empleado():
    u = Universidad([], [], [])
    profesor_titular = Profesor_titular('nombre', '123456789A', 'direccion', 'V', EDepartamento.DIIC, [123, 456], 'area')
    u.anadir_empleado(profesor_titular)
    u.eliminar_empleado('123456789A')
    assert profesor_titular not in u.empleados

def test_eliminar_estudiante():
    u = Universidad([], [])
    estudiante = Estudiante('nombre', '123456789A', 'direccion', 'V', [123, 456])
    u.anadir_estudiante(estudiante)
    u.eliminar_estudiante('123456789A')
    assert estudiante not in u.estudiantes

def test_eliminar_asignatura():
    u = Universidad([], [])
    asignatura = Asignatura('a', 123, 6, 36)
    u.anadir_asignatura(asignatura)
    u.eliminar_asignatura(123)
    assert asignatura not in u.asignaturas

if __name__ == '__main__':
    pytest.main()