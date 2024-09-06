import json
from usuario import Usuario
from datetime import datetime
import os

# Lista que contendrá los objetos de tipo Usuario
lista = []

try:
    # Intenta abrir el archivo 'usuarios.txt'
    with open("usuarios.txt") as usuarios:
        # Recorre cada línea del archivo
        for linea in usuarios:
            try:
                # Convierte la línea del archivo de formato JSON a un diccionario
                usuario = json.loads(linea)
                
                # Crea una instancia de la clase Usuario con los datos obtenidos
                nuevo_usuario = Usuario(usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"])
                
                # Agrega el nuevo usuario a la lista
                lista.append(nuevo_usuario)
                
            except Exception as e:
                """
                Captura cualquier excepción que ocurra durante el procesamiento de las líneas.
                Registra el error en el archivo 'error.log' con la fecha y hora.
                
                Args:
                    e (Exception): El error capturado.
                """
                # Obtiene la fecha y hora actual
                fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Convierte el error a cadena de texto
                texto_error = str(e)
                
                # Genera el mensaje de error que será registrado
                linea_error = f"{fecha_hora}- error detectado!!!: {texto_error}\n"
                
                # Abre el archivo 'error.log' en modo de añadir y registra el error
                with open("error.log", "a+") as log:
                    log.write(linea_error)
                    log.close

    # Limpia la consola, dependiendo del sistema operativo
    os.system("cls") if os.name == "nt" else os.system("clear")
    
    # Imprime la información de cada usuario en la lista
    for persona in lista:
        print(persona)

except FileNotFoundError:
    """
    Captura la excepción cuando el archivo 'usuarios.txt' no se encuentra.
    """
    print("No se ha encontrado el archivo")