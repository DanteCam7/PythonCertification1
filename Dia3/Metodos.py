texto = "Este es el texto de Dante el magnifico"
texto2 = "Y Mimi es la mejor ingeniera quesera"
texto3 = "La amo, y me va a dar muchos quesos <3"

r1 = texto[2:10].upper()
r2 = texto.lower()
r3 = texto.split("t") #adentro va el separador
r4 = "-".join([texto,texto2,texto3]) #Al inicio defino el separador
r5 = texto.find("Dante")
r6 = texto.replace("es", "wololo")

print(r6)