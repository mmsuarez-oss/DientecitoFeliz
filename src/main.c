/*
 * Dientecito Feliz - v0.1 (Prototipo basico)
 * Presentacion: Lunes 12 de octubre
 *
 * Flujo que debe correr de principio a fin:
 *   iniciar sesion -> ver menu segun el rol -> registrar un paciente -> listarlo
 *
 * Todavia NO incluye (se agrega en versiones siguientes):
 *   archivos, validaciones de datos, busqueda, limite de intentos de login.
 *
 * Reparto de funciones (cronograma v0.1):
 *   Camilo Cruz        -> main, pantalla de inicio, login
 *   Miguel Suarez       -> registrar paciente (en memoria)
 *   Carlos Castillo     -> listar pacientes, menu del Docente
 *   Reynaldo Mondragon  -> menu Estudiante, menu Administrador, usuarios de prueba
 */

#include <stdio.h>
#include <string.h>

#define MAX_USUARIOS 3
#define MAX_PACIENTES 100
#define LARGO_TEXTO 50

/* Registro de usuario: cuenta de prueba + su rol en el sistema. */
typedef struct {
    char usuario[LARGO_TEXTO];
    char clave[LARGO_TEXTO];
    char rol[20]; /* "Estudiante", "Docente" o "Administrador" */
} Usuario;

/* Registro de paciente: solo los datos basicos que pide la v0.1. */
typedef struct {
    char nombre[LARGO_TEXTO];
    char cedula[20];
    char telefono[15];
} Paciente;

/* ---------- Reynaldo Mondragon: usuarios de prueba (uno por rol) ---------- */
void cargarUsuariosDePrueba(Usuario usuarios[], int *totalUsuarios) {
    strcpy(usuarios[0].usuario, "estudiante");
    strcpy(usuarios[0].clave, "1234");
    strcpy(usuarios[0].rol, "Estudiante");

    strcpy(usuarios[1].usuario, "docente");
    strcpy(usuarios[1].clave, "1234");
    strcpy(usuarios[1].rol, "Docente");

    strcpy(usuarios[2].usuario, "admin");
    strcpy(usuarios[2].clave, "1234");
    strcpy(usuarios[2].rol, "Administrador");

    *totalUsuarios = MAX_USUARIOS;
}

/* ---------- Camilo Cruz: login simple (sin limite de intentos aun) ----------
 * Recibe: el arreglo de usuarios de prueba y su total.
 * Devuelve: puntero al Usuario que inicio sesion, o NULL si no coincide.
 */
Usuario *iniciarSesion(Usuario usuarios[], int totalUsuarios) {
    char usuario[LARGO_TEXTO];
    char clave[LARGO_TEXTO];

    printf("Usuario: ");
    scanf("%49s", usuario);
    printf("Clave: ");
    scanf("%49s", clave);

    for (int i = 0; i < totalUsuarios; i++) {
        if (strcmp(usuarios[i].usuario, usuario) == 0 &&
            strcmp(usuarios[i].clave, clave) == 0) {
            return &usuarios[i];
        }
    }
    return NULL;
}

/* ---------- Miguel Suarez: registrar paciente en memoria, sin validaciones ----------
 * Recibe: el arreglo de pacientes y su total actual (por referencia).
 * Devuelve: nada; agrega el paciente al arreglo si hay espacio.
 */
void registrarPaciente(Paciente pacientes[], int *totalPacientes) {
    if (*totalPacientes >= MAX_PACIENTES) {
        printf("\nYa no hay espacio para mas pacientes en esta version.\n");
        return;
    }

    Paciente nuevo;
    printf("\n-- Registrar paciente --\n");
    printf("Nombre: ");
    scanf(" %49[^\n]", nuevo.nombre);
    printf("Cedula: ");
    scanf(" %19[^\n]", nuevo.cedula);
    printf("Telefono: ");
    scanf(" %14[^\n]", nuevo.telefono);

    pacientes[*totalPacientes] = nuevo;
    (*totalPacientes)++;
    printf("Paciente registrado.\n");
}

/* ---------- Carlos Castillo: listar pacientes ----------
 * Recibe: el arreglo de pacientes y su total.
 * Devuelve: nada; imprime la lista en pantalla.
 */
void listarPacientes(Paciente pacientes[], int totalPacientes) {
    printf("\n-- Lista de pacientes (%d) --\n", totalPacientes);
    if (totalPacientes == 0) {
        printf("Todavia no hay pacientes registrados.\n");
        return;
    }
    for (int i = 0; i < totalPacientes; i++) {
        printf("%d. %-25s cedula: %-18s tel: %s\n",
               i + 1, pacientes[i].nombre, pacientes[i].cedula, pacientes[i].telefono);
    }
}

void enConstruccion(void) {
    printf("\nEn construccion.\n");
}

/* ---------- Carlos Castillo: menu del Docente (opciones visibles) ---------- */
void menuDocente(Paciente pacientes[], int *totalPacientes) {
    int opcion;
    do {
        printf("\n=== Menu Docente ===\n");
        printf("1. Registrar paciente\n");
        printf("2. Listar pacientes\n");
        printf("3. Aprobar pacientes (en construccion)\n");
        printf("4. Expediente clinico (en construccion)\n");
        printf("0. Salir\n");
        printf("Opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1: registrarPaciente(pacientes, totalPacientes); break;
            case 2: listarPacientes(pacientes, *totalPacientes); break;
            case 3: enConstruccion(); break;
            case 4: enConstruccion(); break;
            case 0: printf("Cerrando sesion...\n"); break;
            default: printf("Opcion invalida.\n");
        }
    } while (opcion != 0);
}

/* ---------- Reynaldo Mondragon: menu del Estudiante ---------- */
void menuEstudiante(Paciente pacientes[], int *totalPacientes) {
    int opcion;
    do {
        printf("\n=== Menu Estudiante ===\n");
        printf("1. Registrar paciente\n");
        printf("2. Listar pacientes\n");
        printf("3. Agendar cita (en construccion)\n");
        printf("4. Odontograma (en construccion)\n");
        printf("0. Salir\n");
        printf("Opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1: registrarPaciente(pacientes, totalPacientes); break;
            case 2: listarPacientes(pacientes, *totalPacientes); break;
            case 3: enConstruccion(); break;
            case 4: enConstruccion(); break;
            case 0: printf("Cerrando sesion...\n"); break;
            default: printf("Opcion invalida.\n");
        }
    } while (opcion != 0);
}

/* ---------- Reynaldo Mondragon: menu del Administrador ---------- */
void menuAdministrador(Paciente pacientes[], int *totalPacientes) {
    int opcion;
    do {
        printf("\n=== Menu Administrador ===\n");
        printf("1. Listar pacientes\n");
        printf("2. Gestionar usuarios (en construccion)\n");
        printf("3. Ver bitacora (en construccion)\n");
        printf("0. Salir\n");
        printf("Opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1: listarPacientes(pacientes, *totalPacientes); break;
            case 2: enConstruccion(); break;
            case 3: enConstruccion(); break;
            case 0: printf("Cerrando sesion...\n"); break;
            default: printf("Opcion invalida.\n");
        }
    } while (opcion != 0);
}

/* ---------- Camilo Cruz: main / pantalla de inicio ---------- */
int main(void) {
    Usuario usuarios[MAX_USUARIOS];
    int totalUsuarios = 0;
    cargarUsuariosDePrueba(usuarios, &totalUsuarios);

    Paciente pacientes[MAX_PACIENTES];
    int totalPacientes = 0;

    printf("=====================================\n");
    printf("      DIENTECITO FELIZ - v0.1\n");
    printf("=====================================\n");

    Usuario *sesion = iniciarSesion(usuarios, totalUsuarios);
    if (sesion == NULL) {
        printf("\nUsuario o clave incorrectos. Programa finalizado.\n");
        return 1;
    }

    printf("\nBienvenido, %s (%s)\n", sesion->usuario, sesion->rol);

    if (strcmp(sesion->rol, "Docente") == 0) {
        menuDocente(pacientes, &totalPacientes);
    } else if (strcmp(sesion->rol, "Administrador") == 0) {
        menuAdministrador(pacientes, &totalPacientes);
    } else {
        menuEstudiante(pacientes, &totalPacientes);
    }

    printf("\nHasta luego.\n");
    return 0;
}
