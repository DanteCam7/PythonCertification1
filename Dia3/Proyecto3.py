text = input("Dame un texto a analizar: ")
letra = []
letras = input("Ingresa 3 letras a tu elección: ")
letra.append(letras[0])
letra.append(letras[1])
letra.append(letras[2])
text_list = text.split(" ")

letra1 = text.lower().count(letra[0])
letra2 = text.lower().count(letra[1])
letra3 = text.lower().count(letra[2])

print(f"La letra {letra[0]} se repite {letra1} veces\nLa letra {letra[1]} se repite {letra2} veces\nLa letra {letra[2]} se repite {letra3} veces")

print(len(text_list))

print(f"La primer letra es '{text[0]}' y la última letra es '{text[-1]}'")
text_list.reverse()
text_reverse = " ".join(text_list)
print(text_reverse)

print(text.find("Python") != -1)
dic = {True:"Si está", False: "No está"}
print(f"La palabra 'Python' {dic['Python' in text]}")


