def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Sirf number dalo.")


print("===== CALCULATOR =====")

while True:
    print("\nOperations:")
    print("1. Jodna        (+)")
    print("2. Ghatana      (-)")
    print("3. Guna         (*)")
    print("4. Divide       (/)")
    print("5. Floor divide (//)")
    print("6. Remainder    (%)")
    print("7. Power        (**)")
    print("8. Exit")

    choice = input("Option chuno (1-8): ").strip()

    if choice == "8":
        print("Thank you! Bye.")
        break

    if choice not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Galat option, dobara try karo.")
        continue

    a = get_number("Pehla number: ")
    b = get_number("Dusra number: ")

    if choice == "1":
        print(f"{a} + {b} = {a + b}")
    elif choice == "2":
        print(f"{a} - {b} = {a - b}")
    elif choice == "3":
        print(f"{a} * {b} = {a * b}")
    elif choice == "4":
        if b == 0:
            print("Error: 0 se divide nahi kar sakte.")
        else:
            print(f"{a} / {b} = {a / b}")
    elif choice == "5":
        if b == 0:
            print("Error: 0 se divide nahi kar sakte.")
        else:
            print(f"{a} // {b} = {a // b}")
    elif choice == "6":
        if b == 0:
            print("Error: 0 se divide nahi kar sakte.")
        else:
            print(f"{a} % {b} = {a % b}")
    elif choice == "7":
        print(f"{a} ** {b} = {a ** b}")
