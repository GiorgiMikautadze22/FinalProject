class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.addresses = []

    def place_order(self, order):
        self.orders.append(order)

    def add_address(self, address):
        self.addresses.append(address)