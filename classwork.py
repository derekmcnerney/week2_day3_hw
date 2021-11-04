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
            name, price = item  # or price = item[1]
            total = total + price

    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count

    def removeItem(self, item):
    #removes the item from the cart's item list


def main():
    
    cart = cart()

    done = false

    while not done:

    
main()
