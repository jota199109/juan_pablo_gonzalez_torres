from datetime import datetime

def registrar_proceso():
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Proceso informático ejecutado correctamente: {fecha}")

if __name__ == "__main__":
    registrar_proceso()