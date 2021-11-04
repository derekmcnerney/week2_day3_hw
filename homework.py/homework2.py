def show_instructions():
    print("""Type 'add' to add new items to your shopping cart.
Type 'quit' to exit the program.
Type 'show' to list all items in your shopping cart.""")
    print("<3"*30)


def Cart():
    input('Welcome to Hello Kitty! Press any key to continue. ')
    print("<3"*30)


class Item:
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
        


        def main():
            item1 = Item("name", "price", "quantity")
            item2 = Item("name", "price", "quantity")
            item3 = Item("name", "price", "quantity")
            c = Cart()
            c.addItem(item1)
            c.addItem(item2)
            c.addItem(item3)
            print("You have %i items in your cart for a total of $%.02f" % (c.getNumItems(), c.getTotal())



        main()

class Item:
    def __init__(self, item, price, quantity,):
        self.item = item
        self.price = price
        self.quantity = quantity
        

    def print_info(self):
        print(f"{self.item} ${self.price} {self.quantity}")
