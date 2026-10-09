"""
Dientecito Feliz - v0.1 (Prototipo basico, version web local)
Presentacion: Lunes 12 de octubre

Flujo que debe correr de principio a fin:
  iniciar sesion -> ver menu segun el rol -> registrar un paciente -> listarlo

Todavia NO incluye (se agrega en versiones siguientes):
  archivos, validaciones de datos, busqueda, limite de intentos de login.

Reparto de funciones (cronograma v0.1):
  Camilo Cruz        -> app/main, pantalla de inicio, login
  Miguel Suarez       -> registrar paciente (en memoria)
  Carlos Castillo     -> listar pacientes, menu del Docente
  Reynaldo Mondragon  -> menu Estudiante, menu Administrador, usuarios de prueba

Ejecutar: python src/app.py  ->  abrir http://localhost:5000
"""

from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "dientecito-feliz-v0.1"  # solo para la sesion local de desarrollo

USUARIOS_DE_PRUEBA = [
    {"usuario": "estudiante", "clave": "1234", "rol": "Estudiante"},
    {"usuario": "docente", "clave": "1234", "rol": "Docente"},
    {"usuario": "admin", "clave": "1234", "rol": "Administrador"},
]

PACIENTES = []  # en memoria, sin archivos todavia (se agrega en v0.3)

BASE = """
<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Dientecito Feliz</title>
<style>
  body { font-family: Arial, sans-serif; background:#f4f5f7; color:#222; margin:0; }
  .app { max-width: 640px; margin: 30px auto; background:#fff; border:1px solid #cfd3d8; padding:20px; }
  h1 { color:#2b4a6f; font-size:20px; }
  nav a { display:inline-block; margin:4px 8px 4px 0; padding:6px 12px; background:#f3f4f6;
          border:1px solid #b8bcc2; border-radius:3px; text-decoration:none; color:#222; }
  nav a:hover { background:#eef2f6; }
  table { border-collapse: collapse; width:100%; margin-top:10px; }
  th, td { border:1px solid #cfd3d8; padding:6px 8px; text-align:left; font-size:14px; }
  label { display:block; margin-top:10px; font-size:14px; }
  input { width:100%; padding:6px; margin-top:4px; box-sizing:border-box; }
  button { margin-top:14px; padding:8px 16px; background:#2b4a6f; color:#fff; border:0; border-radius:3px; cursor:pointer; }
  .tenue { color:#6b6f75; font-size:13px; }
  .error { color:#9b2c2c; }
</style></head>
<body><div class="app">
<h1>Dientecito Feliz - v0.1</h1>
{{ body|safe }}
</div></body></html>
"""


def pagina(body):
    return render_template_string(BASE, body=body)


def menu_html(sesion, opciones):
    """Arma el menu segun el rol con sus opciones visibles.
    Recibe: datos de la sesion y lista de (texto, ruta) del menu.
    Devuelve: fragmento HTML del menu.
    """
    links = "".join(f'<a href="{ruta}">{texto}</a>' for texto, ruta in opciones)
    return f"""
    <p class="tenue">Sesion: {sesion['usuario']} ({sesion['rol']})
      &middot; <a href="{url_for('logout')}">Salir</a></p>
    <nav>{links}</nav>
    """


# ---------- Camilo Cruz: login simple (sin limite de intentos aun) ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        clave = request.form.get("clave", "")
        for u in USUARIOS_DE_PRUEBA:
            if u["usuario"] == usuario and u["clave"] == clave:
                session["usuario"] = u["usuario"]
                session["rol"] = u["rol"]
                return redirect(url_for("menu"))
        error = '<p class="error">Usuario o clave incorrectos.</p>'

    return pagina(f"""
    {error}
    <form method="post">
      <label>Usuario <input name="usuario" autofocus></label>
      <label>Clave <input name="clave" type="password"></label>
      <button type="submit">Iniciar sesion</button>
    </form>
    <p class="tenue">Usuarios de prueba: estudiante/1234, docente/1234, admin/1234</p>
    """)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------- Camilo Cruz: menu segun el rol ----------
@app.route("/")
@app.route("/menu")
def menu():
    if "rol" not in session:
        return redirect(url_for("login"))

    rol = session["rol"]
    if rol == "Docente":
        opciones = [
            ("Registrar paciente", url_for("registrar_paciente")),
            ("Listar pacientes", url_for("listar_pacientes")),
            ("Aprobar pacientes (en construccion)", url_for("en_construccion")),
            ("Expediente clinico (en construccion)", url_for("en_construccion")),
        ]
    elif rol == "Administrador":
        opciones = [
            ("Listar pacientes", url_for("listar_pacientes")),
            ("Gestionar usuarios (en construccion)", url_for("en_construccion")),
            ("Ver bitacora (en construccion)", url_for("en_construccion")),
        ]
    else:  # Estudiante
        opciones = [
            ("Registrar paciente", url_for("registrar_paciente")),
            ("Listar pacientes", url_for("listar_pacientes")),
            ("Agendar cita (en construccion)", url_for("en_construccion")),
            ("Odontograma (en construccion)", url_for("en_construccion")),
        ]

    return pagina(f"<h2>Menu {rol}</h2>" + menu_html(session, opciones))


# ---------- Miguel Suarez: registrar paciente en memoria, sin validaciones ----------
@app.route("/pacientes/nuevo", methods=["GET", "POST"])
def registrar_paciente():
    if "rol" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        PACIENTES.append({
            "nombre": request.form.get("nombre", ""),
            "cedula": request.form.get("cedula", ""),
            "telefono": request.form.get("telefono", ""),
        })
        return redirect(url_for("listar_pacientes"))

    return pagina(f"""
    {menu_html(session, [("Volver al menu", url_for("menu"))])}
    <h2>Registrar paciente</h2>
    <form method="post">
      <label>Nombre <input name="nombre" autofocus></label>
      <label>Cedula <input name="cedula"></label>
      <label>Telefono <input name="telefono"></label>
      <button type="submit">Registrar</button>
    </form>
    """)


# ---------- Carlos Castillo: listar pacientes ----------
@app.route("/pacientes")
def listar_pacientes():
    if "rol" not in session:
        return redirect(url_for("login"))

    if PACIENTES:
        filas = "".join(
            f"<tr><td>{i}</td><td>{p['nombre']}</td><td>{p['cedula']}</td><td>{p['telefono']}</td></tr>"
            for i, p in enumerate(PACIENTES, start=1)
        )
        tabla = f"""<table>
          <tr><th>#</th><th>Nombre</th><th>Cedula</th><th>Telefono</th></tr>
          {filas}
        </table>"""
    else:
        tabla = "<p>Todavia no hay pacientes registrados.</p>"

    return pagina(f"""
    {menu_html(session, [("Volver al menu", url_for("menu"))])}
    <h2>Pacientes ({len(PACIENTES)})</h2>
    {tabla}
    """)


@app.route("/en-construccion")
def en_construccion():
    if "rol" not in session:
        return redirect(url_for("login"))
    return pagina(f"""
    {menu_html(session, [("Volver al menu", url_for("menu"))])}
    <h2>En construccion</h2>
    """)


if __name__ == "__main__":
    app.run(debug=True)
