# Problem 1

def show_instructions():
    print("""Type 'add' to add new items to your shopping cart.
Type 'quit' to exit the program.
Type 'show' to list all items in your shopping cart.""")
    print("<3"*30)


def Cart():
    input('Welcome to Hello Kitty! Press any key to continue. ')
    print("<3"*30)

    class Item:

        def __init__(self, item, price, quantity,):
            self.item = your_item
            self.price = price
            self.quantity = quantity

    def print_info(self):
        print(f"{self.item} ${self.price} {self.quantity}")

    

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name


class Cart:
    def __init__(self, list):
        self.list = []

    def addItem(self, item):
        self.list.append(self.list)

    def getTotal(self):
        total = 0
        for item in self.list:
            name, price = item  
            total = total + price

    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count

    def removeItem(self, item):
        done = False
    
    
    show_instructions()
    
    
    
    while not done:

        choice = input(
            "What is your choice? Add | Remove | Show | Quit? ").lower()
        if choice == 'add':
            your_item = input(
                "Type in the item you wish to purchase. ").title()
            price = input(
                "What is the price of your product").title()
            quantity = input(
                "How many would you like to purchase").title()
            
            Item = {
                'Name': your_item, 'Price': price, 'quantity': quantity

            }
            Cart.append(Item)
        elif choice == 'remove':
            your_item = input(
                "Type in the item you wish to remove. ").title()

            Item = {
                'Name': your_item, 'Price': price, 'quantity': quantity
            }

            Cart.remove(Item)

        elif choice == 'show':
            for item in Cart:
                print(item)
            input('Press any key to continue ')
        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                done = True
                for item in Cart:
                    print(item)
                    print("Have a good day. Bye!")
            elif confirm == 'n':
                continue

Cart()