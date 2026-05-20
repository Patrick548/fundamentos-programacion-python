# ==============================
#     SISTEMA DE CONTRATOS
# ==============================

# ----- Datos precargados -----
clientes = ["Juan Perez", "Empresa ABC"]
fechas_venc = ["2024-05-30", "2024-06-15"]
montos = [2500.0, 4800.0]
estados = ["Activo", "Activo"]

# ==============================
# VALIDACIONES
# ==============================

def validar_fecha(fecha):
    # Formato esperado: AAAA-MM-DD
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    año, mes, dia = partes
    if not (año.isdigit() and mes.isdigit() and dia.isdigit()):
        return False
    if int(mes) < 1 or int(mes) > 12:
        return False
    if int(dia) < 1 or int(dia) > 31:
        return False
    return True


def validar_monto(texto):
    try:
        valor = float(texto)
        return valor >= 0
    except:
        return False


# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def registrar_contrato():
    print("\n=== REGISTRAR NUEVO CONTRATO ===")
    nombre = input("Ingrese nombre del cliente: ").strip()

    fecha = input("Ingrese fecha de vencimiento (AAAA-MM-DD): ").strip()
    # Validación de fecha
    while not validar_fecha(fecha):
        print("❌ Fecha inválida. Intente nuevamente.")
        fecha = input("Ingrese fecha de vencimiento (AAAA-MM-DD): ").strip()

    monto_txt = input("Ingrese monto del contrato: ").strip()
    # Validación de monto
    while not validar_monto(monto_txt):
        print("❌ Monto inválido. Ingrese solo números.")
        monto_txt = input("Ingrese monto del contrato: ").strip()

    monto = float(monto_txt)

    # Registrar
    clientes.append(nombre)
    fechas_venc.append(fecha)
    montos.append(monto)
    estados.append("Activo")

    print("✔ Contrato registrado correctamente.\n")


def registrar_renovacion():
    print("\n=== REGISTRAR RENOVACIÓN ===")
    
    if len(clientes) == 0:
        print("No hay contratos registrados.")
        return

    # Mostrar lista
    for i in range(len(clientes)):
        print(f"{i + 1}. {clientes[i]} - Vence: {fechas_venc[i]}")

    opc_txt = input("Seleccione el número del contrato: ").strip()
    while not (opc_txt.isdigit() and 1 <= int(opc_txt) <= len(clientes)):
        print("❌ Opción inválida.")
        opc_txt = input("Seleccione el número del contrato: ").strip()

    i = int(opc_txt) - 1

    # Nueva fecha
    nueva_fecha = input("Nueva fecha de vencimiento (AAAA-MM-DD): ").strip()
    while not validar_fecha(nueva_fecha):
        print("❌ Fecha inválida.")
        nueva_fecha = input("Nueva fecha de vencimiento (AAAA-MM-DD): ").strip()

    # Nuevo monto
    nuevo_monto_txt = input("Nuevo monto del contrato: ").strip()
    while not validar_monto(nuevo_monto_txt):
        print("❌ Monto inválido.")
        nuevo_monto_txt = input("Nuevo monto del contrato: ").strip()

    nuevo_monto = float(nuevo_monto_txt)

    # Guardar cambios
    fechas_venc[i] = nueva_fecha
    montos[i] = nuevo_monto
    estados[i] = "Renovado"

    print("✔ Renovación registrada correctamente.\n")


def mostrar_reportes():
    print("\n=== REPORTE GENERAL DE CONTRATOS ===")

    if len(clientes) == 0:
        print("No hay contratos para mostrar.")
        return

    for i in range(len(clientes)):
        print("-------------------------------------")
        print(f"Cliente: {clientes[i]}")
        print(f"Fecha de vencimiento: {fechas_venc[i]}")
        print(f"Monto: S/ {montos[i]}")
        print(f"Estado: {estados[i]}")
    print("-------------------------------------\n")


# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu():
    while True:
        print("==================================")
        print("   SISTEMA DE CONTROL DE CONTRATOS")
        print("==================================")
        print("1. Registrar contrato")
        print("2. Registrar renovación")
        print("3. Mostrar reportes")
        print("4. Salir")
        print("----------------------------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_contrato()
        elif opcion == "2":
            registrar_renovacion()
        elif opcion == "3":
            mostrar_reportes()
        elif opcion == "4":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.\n")


# ==============================
# INICIAR PROGRAMA
# ==============================
menu()