#inventario en lista de diccionarios
inventory = []

#añade un nuevo producto al inventario
def add_product():
    name = input("Pon el nombre del producto: ").strip()
    if any(product["name"] == name for product in inventory):
        print("Ese producto ya existe.")
        return
    
    try:
        price = float(input("Pon el precio del producto: "))
        quantity = int(input("Pon la cantidad disponible: "))
        inventory.append({"name": name, "price": price, "quantity": quantity})
        print("Producto agregado.")
    except ValueError:
        print("Pon un número válido para el precio y cantidad.")

#consulta un producto por nombre y muestra su información
def search_product():
    name = input("Pon el nombre del producto a buscar: ").strip()
    for product in inventory:
        if product["name"] == name:
            print(f"Precio: {product['price']}, Cantidad disponible: {product['quantity']}")
            return
    print("Producto no encontrado.")

#actualiza el precio de un producto existente
def update_price():
    name = input("Pon el nombre del producto a actualizar: ").strip()
    for product in inventory:
        if product["name"] == name:
            try:
                new_price = float(input("Pon el nuevo precio: "))
                product["price"] = new_price
                print("Precio actualizado.")
                return
            except ValueError:
                print("Precio inválido.")
                return
    print("Producto no encontrado.")

#elimina un producto del inventario
def delete_product():
    name = input("Pon el nombre del producto a eliminar: ").strip()
    for i, product in enumerate(inventory):
        if product["name"] == name:
            inventory.pop(i)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

#calcula y muestra el valor total del inventario
def calculate_total_value():
    total = sum(map(lambda product: product["price"] * product["quantity"], inventory))
    print(f"El valor total del inventario es: {total:.2f}")

#muestra el menú y permite seleccionar operaciones
def show_menu():
    while True:
        print("\nTIENDA JERÓNIMO")
        print("(A) Añadir producto")
        print("(B) Buscar producto")
        print("(C) Actualizar precio")
        print("(E) Eliminar producto")
        print("(V) Valor total de todo")
        print("(S) Salir")

        option = input("Selecciona una opción: ").strip().upper()

        if option == "A":
            add_product()
        elif option == "B":
            search_product()
        elif option == "C":
            update_price()
        elif option == "E":
            delete_product()
        elif option == "V":
            calculate_total_value()
        elif option == "S":
            print("Adiós Jerónimo.")
            break
        else:
            print("Pon una opción válida.")

show_menu()
