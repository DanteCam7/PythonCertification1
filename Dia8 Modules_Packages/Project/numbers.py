def perfumery_numbers():
    for n in range(1, 1000):
        yield f"P - {n}"


def pharmacy_numbers():
    for n in range(1, 1000):
        yield f"F - {n}"


def cosmetic_numbers():
    for n in range(1, 1000):
        yield f"C - {n}"


p = perfumery_numbers()
f = pharmacy_numbers()
c = cosmetic_numbers()


def decorator(rubro):
    print("\n" + "*" * 23)
    print("Your number is:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Please wait for your turn")
    print("*" * 23 + "\n")
