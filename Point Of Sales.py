# This function adds a new product and its price to the products list.
def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: R"))

    # The product name and price are stored together in the products list.
    products.append([name, price])

    print("Product added successfully!")


# This function calculates the total price of all products.
def calculate_total(products):
    total = 0

    # This for loop goes through every product in the products list.
    for product in products:
        # Add the price of the current product to the total.
        total = total + product[1]

    # Return the calculated total to the function that called it.
    return total


# This function displays all the products, their prices and the total.
def display_products(products):
    print()
    print("--- PRODUCTS ---")

    # This for loop displays every product stored in the list.
    for product in products:
        name = product[0]
        price = product[1]

        # Display the product name and price.
        print(name, "R{:.2f}".format(price))

    # Call the calculate_total function to calculate the total.
    total = calculate_total(products)

    # Display the total price.
    print("----------------")
    print("Total R{:.2f}".format(total))


# This function removes all products from the products list.
def clear_products(products):
    products.clear()

    print("All products have been removed.")


# This function clears the output from the Windows CMD screen.
def clear_screen():
    import os

    # "cls" is the command used by Windows CMD to clear the screen.
    os.system("cls")


# This function displays the POS menu.
def display_menu():
    print()
    print("======================")
    print("       PYTHON POS")
    print("======================")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Clear Products")
    print("4. Clear Screen")
    print("5. Exit")
    print("======================")


# This is the main function that controls the POS program.
def main():

    # This list stores every product entered by the user.
    products = []

    # This is the sentinel variable.
    # The program continues while exit_program is False.
    exit_program = False

    # This while loop keeps the POS running until the user chooses Exit.
    while exit_program == False:

        # Display the POS menu.
        display_menu()

        # Ask the user to choose an option.
        choice = input("Enter your choice: ")

        # Option 1 adds a product.
        if choice == "1":
            add_product(products)

        # Option 2 displays all products and the total.
        elif choice == "2":
            display_products(products)

        # Option 3 removes all products.
        elif choice == "3":
            clear_products(products)

        # Option 4 clears the CMD screen.
        elif choice == "4":
            clear_screen()

        # Option 5 exits the POS.
        elif choice == "5":
            # Change the sentinel variable to True.
            # This causes the while loop to stop.
            exit_program = True

            print("Thank you for using the POS!")

        # This handles an invalid menu choice.
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# This starts the POS program by calling the main function.
main()