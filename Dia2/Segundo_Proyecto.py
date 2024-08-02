nombre = input("¿Cómo te llamas?")
monto = float(input("¿Cuáles fueron tus ventas totales?"))

comisiones = round(monto * 0.13,2)

print(f"Hola {nombre}, tus ventas de este mes han sido de ${monto}, por lo que tus comisiones son de ${comisiones}")
