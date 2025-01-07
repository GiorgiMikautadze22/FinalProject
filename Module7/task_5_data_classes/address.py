class Address:
    def __init__(self, address, address_line_1, address_line_2, city, state, postal_code, country):
        self.address_id = 0
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.shipments = []

    def add_shipment(self, order):
        self.shipments.append(order)