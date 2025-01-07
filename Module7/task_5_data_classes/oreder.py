class Order:
    def __init__(self, customer, address):
        self.customer = customer
        self.address = address

        address.add_shipment(self)