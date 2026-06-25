import json

FILE_NAME = "inventory.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"products": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_product():
    
    data = load_data()

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    data["products"].append(product)

    save_data(data)

    print("Product added successfully.")


def view_products():
    
    data = load_data()

    if len(data["products"]) == 0:
        print("No products found.")
        return

    print("\n----- PRODUCTS -----")

    for index, product in enumerate(data["products"], start=1):

        print(
            f"{index}. "
            f"Name: {product['name']} | "
            f"Price: {product['price']} | "
            f"Stock: {product['stock']}"
        )


def search_product():
    
    data = load_data()

    product_name = input("Enter product name: ")

    for product in data["products"]:

        if product["name"].lower() == product_name.lower():

            print(
                f"Name: {product['name']} | "
                f"Price: {product['price']} | "
                f"Stock: {product['stock']}"
            )

            return

    print("Product not found.")


def update_stock():
    
    data = load_data()

    product_name = input("Enter product name: ")

    for product in data["products"]:

        if product["name"].lower() == product_name.lower():

            new_stock = int(input("Enter new stock quantity: "))

            product["stock"] = new_stock

            save_data(data)

            print("Stock updated successfully.")

            return

    print("Product not found.")


def delete_product():
    
    data = load_data()

    if len(data["products"]) == 0:
        print("No products found.")
        return

    print("\n----- PRODUCTS -----")

    for index, product in enumerate(data["products"], start=1):

        print(
            f"{index}. "
            f"Name: {product['name']} | "
            f"Price: {product['price']} | "
            f"Stock: {product['stock']}"
        )

    try:

        choice = int(input("Enter product number to delete: "))

        deleted_product = data["products"].pop(choice - 1)

        save_data(data)

        print(f"Deleted: {deleted_product['name']}")

    except (ValueError, IndexError):

        print("Invalid selection.")


def menu():

    while True:

        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


menu()