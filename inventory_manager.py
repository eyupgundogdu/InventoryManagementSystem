class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f'Name: {self.name} | Price: {self.price} | Quantity: {self.quantity}'

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_product(self):
        name = input('Name: ')
        price = int(input('Price: '))
        quantity = int(input('Quantity: '))
        new_item = Product(name,price,quantity)
        self.inventory.append(new_item)


    def list_inventory(self):
        for i in self.inventory:
            print(i)

    def sell_product(self):
        item = input('Enter item name you want to sell: ')
        found = False
        for i in self.inventory:
            if i.name.lower() == item.lower():
                found = True
                if i.quantity > 0:
                    i.quantity -= 1
                    print('Sold')
                else:
                    print('Out of stock')
        if not found:
            print('There is no such an item in our inventory!')


    def total_value(self):
        total = 0
        for i in self.inventory:
            total_price = i.price * i.quantity
            total += total_price
        print(f'Total Value: {total}')

    def restock_low_stock(self):
        for i in self.inventory:
            if i.quantity < 3:
                print(f'Kritik stok: {i.name}')


def main():
    item = Inventory()

    while True:
        choice = input('1 - Add Product\n2 - List Inventory\n3 - Sell Product\n4 - Total value\n5 - Restock\n6 - Exit\nChoice: ')
        if choice == '1':
            item.add_product()
        elif choice == '2':
            item.list_inventory()
        elif choice == '3':
            item.sell_product()
        elif choice == '4':
            item.total_value()
        elif choice == '5':
            item.restock_low_stock()
        elif choice == '6':
            break
        else:
            print('Invalid Choice.')


if __name__ == '__main__':
    main()