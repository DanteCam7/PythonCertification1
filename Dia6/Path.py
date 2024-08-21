from pathlib import Path

base = Path.home()
guia = Path(base,"Europa", "España", Path("Barcelona", "Sagrada Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)

print(guia.parent.parent)

print('------------------------------------------------------------')

guia3 = Path(Path.home(),'Europa')

for txt in guia3.glob("*.txt"):
    print(txt)
print('------------------------------------------------------------')
#buscar en subcarpetas
for txt in guia3.glob("**/*.txt"):
    print(txt)

print('------------------------------------------------------------')

guia4 = Path("Europa", "España", "Barcelona", "SagradaFamilia.txt")
em_europa = guia4.relative_to(Path("Europa"))
en_españa = guia4.relative_to(Path("Europa", "España"))
print(em_europa)
print(en_españa)



