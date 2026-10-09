# Dientecito Feliz

Sistema web local para la clínica odontológica Dientecito Feliz.
Universidad Americana - Facultad de Ingeniería y Arquitectura - Programación Estructurada.

Desarrollo por versiones según `Cronograma_actualizado_v2.pdf`: cada defensa agrega un módulo
nuevo sobre el anterior, sin romper lo que ya funciona.

## Versión actual: v0.1 (prototipo básico) — Lunes 12 de octubre

Flujo que corre de principio a fin:

```
iniciar sesión -> ver menú según el rol -> registrar un paciente -> listarlo
```

Todavía no incluye: archivos, validaciones, búsqueda ni límite de intentos de login
(se agregan en v0.2 y v0.3).

### Usuarios de prueba (uno por rol)

| Usuario    | Clave | Rol            |
|------------|-------|----------------|
| estudiante | 1234  | Estudiante     |
| docente    | 1234  | Docente        |
| admin      | 1234  | Administrador  |

### Ejecutar

```
pip install -r requirements.txt
python src/app.py
```

Abrir http://localhost:5000 en el navegador.

## Integrantes

- Camilo Cruz
- Miguel Suárez
- Reynaldo Mondragón
- Carlos Castillo

Docente: Carlos Iván Argüello.
