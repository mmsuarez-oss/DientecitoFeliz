"""
Dientecito Feliz - v0.1 (Prototipo basico)
Presentacion: Lunes 12 de octubre

Flujo que debe correr de principio a fin:
  iniciar sesion -> ver menu segun el rol -> registrar un paciente -> listarlo

Todavia NO incluye (se agrega en versiones siguientes):
  archivos, validaciones de datos, busqueda, limite de intentos de login.

Reparto de funciones (cronograma v0.1):
  Camilo Cruz        -> main, pantalla de inicio, login
  Miguel Suarez       -> registrar paciente (en memoria)
  Carlos Castillo     -> listar pacientes, menu del Docente
  Reynaldo Mondragon  -> menu Estudiante, menu Administrador, usuarios de prueba
"""

USUARIOS_DE_PRUEBA = [
    {"usuario": "estudiante", "clave": "1234", "rol": "Estudiante"},
    {"usuario": "docente", "clave": "1234", "rol": "Docente"},
    {"usuario": "admin", "clave": "1234", "rol": "Administrador"},
]


def iniciar_sesion(usuarios):
    """Login simple contra los usuarios de prueba (sin limite de intentos aun).
    Recibe: lista de usuarios de prueba.
    Devuelve: el usuario que inicio sesion, o None si no coincide.
    """
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()
    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == clave:
            return u
    return None


def registrar_paciente(pacientes):
    """Registra un paciente en memoria, sin validaciones.
    Recibe: lista de pacientes.
    Devuelve: nada; agrega el paciente a la lista.
    """
    print("\n-- Registrar paciente --")
    nombre = input("Nombre: ").strip()
    cedula = input("Cedula: ").strip()
    telefono = input("Telefono: ").strip()
    pacientes.append({"nombre": nombre, "cedula": cedula, "telefono": telefono})
    print("Paciente registrado.")


def listar_pacientes(pacientes):
    """Imprime la lista de pacientes registrados.
    Recibe: lista de pacientes.
    Devuelve: nada.
    """
    print(f"\n-- Lista de pacientes ({len(pacientes)}) --")
    if not pacientes:
        print("Todavia no hay pacientes registrados.")
        return
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nombre']:<25} cedula: {p['cedula']:<18} tel: {p['telefono']}")


def en_construccion():
    print("\nEn construccion.")


def _leer_opcion():
    try:
        return int(input("Opcion: "))
    except ValueError:
        return -1


def menu_docente(pacientes):
    """Menu del Docente con sus opciones visibles."""
    opcion = None
    while opcion != 0:
        print("\n=== Menu Docente ===")
        print("1. Registrar paciente")
        print("2. Listar pacientes")
        print("3. Aprobar pacientes (en construccion)")
        print("4. Expediente clinico (en construccion)")
        print("0. Salir")
        opcion = _leer_opcion()

        if opcion == 1:
            registrar_paciente(pacientes)
        elif opcion == 2:
            listar_pacientes(pacientes)
        elif opcion in (3, 4):
            en_construccion()
        elif opcion == 0:
            print("Cerrando sesion...")
        else:
            print("Opcion invalida.")


def menu_estudiante(pacientes):
    """Menu del Estudiante."""
    opcion = None
    while opcion != 0:
        print("\n=== Menu Estudiante ===")
        print("1. Registrar paciente")
        print("2. Listar pacientes")
        print("3. Agendar cita (en construccion)")
        print("4. Odontograma (en construccion)")
        print("0. Salir")
        opcion = _leer_opcion()

        if opcion == 1:
            registrar_paciente(pacientes)
        elif opcion == 2:
            listar_pacientes(pacientes)
        elif opcion in (3, 4):
            en_construccion()
        elif opcion == 0:
            print("Cerrando sesion...")
        else:
            print("Opcion invalida.")


def menu_administrador(pacientes):
    """Menu del Administrador."""
    opcion = None
    while opcion != 0:
        print("\n=== Menu Administrador ===")
        print("1. Listar pacientes")
        print("2. Gestionar usuarios (en construccion)")
        print("3. Ver bitacora (en construccion)")
        print("0. Salir")
        opcion = _leer_opcion()

        if opcion == 1:
            listar_pacientes(pacientes)
        elif opcion in (2, 3):
            en_construccion()
        elif opcion == 0:
            print("Cerrando sesion...")
        else:
            print("Opcion invalida.")


def main():
    pacientes = []

    print("=====================================")
    print("      DIENTECITO FELIZ - v0.1")
    print("=====================================")

    sesion = iniciar_sesion(USUARIOS_DE_PRUEBA)
    if sesion is None:
        print("\nUsuario o clave incorrectos. Programa finalizado.")
        return

    print(f"\nBienvenido, {sesion['usuario']} ({sesion['rol']})")

    if sesion["rol"] == "Docente":
        menu_docente(pacientes)
    elif sesion["rol"] == "Administrador":
        menu_administrador(pacientes)
    else:
        menu_estudiante(pacientes)

    print("\nHasta luego.")


if __name__ == "__main__":
    main()
