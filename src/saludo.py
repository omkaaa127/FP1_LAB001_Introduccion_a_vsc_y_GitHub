from datetime import datetime

hora_actual = datetime.now().hour

nombre = input("¿Cuál es tu nombre?")
if hora_actual <=12:
    print(f"¡Buenos días {nombre}!")
elif hora_actual >=21:
    print(f"¡Buenas noches {nombre}!")
else:
    print(f"¡Buenas tardes {nombre}!")