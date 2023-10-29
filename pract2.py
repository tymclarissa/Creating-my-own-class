class Item:
    def __init__(self, name , price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_item(self,item):
        self.items.append(item)
        self.total_cost += item.price

    def remove_item(self, item):
        if item in self .items:
            self.items.remove(item)
        self.total_cost -= item.price

    def empty_cart(self)
        self . items = []
        self . total_cost = 0
        print("Cart is emptied")

    def print_cart_info(self):
        print(f"The total cost is {self.total_cost}")
        for item in self.items:
            print(f"{item.name} - ${item.price}")