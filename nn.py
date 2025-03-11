def get_name():
    while True:
        try:
            name = input("da: ")


            if not name.isalpha():
                raise ValueError("asdd")

            return name
        except ValueError as e:
            print(e)



name = get_name()
print(f"Привет, {name}!")