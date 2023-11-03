# Librerias usadas: pandas, webbrowser, pyautogui, time
import pandas as pd
import webbrowser
import pyautogui as pg
import time

# Leer la base de datos
data = pd.read_excel("whatsapp/Data/principal.xlsx")
print(data)

# Iteración sobre cada fila de la base de datos
for i in range(len(data)):
    # Personalizamos 
    nombre = data.loc[i, 'Nombres']
    apellido = data.loc[i, 'Apellidos']
    celular = data.loc[i, 'Telefono']

    # Creación del mensaje personalizado
    mensaje = "Aqui va el mensaje (%0A) <- puede usar eso para salto de linea"

    # Abrir una pestana nueva en el navegador para enviar el mensaje por WhatsApp
    webbrowser.open_new_tab("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    # Envio del mensaje
    time.sleep(10)          # Esperar 10 segundos para que cargue la página
    # pg.click(1230, 964)   # Posición del cursor para hacer click en e
    time.sleep(5)           # Esperar 1 segundo
    pg.press('enter')       # Enviar mensaje


    # Cerrar la pestaña
    time.sleep(5)           # Esperar 1.5 a que se envie el mensaje
    pg.hotkey('ctrl', 'w')  # Para cerrar la pestaña
    time.sleep(1)
