class Category:
    def __init__(self, name, parent_category = None):
        self.name = name
        self.subcategories = []
        self.products = []

        if parent_category:
            self.parent_category = parent_category

    def add_product(self, product):
        self.products.append(product)

    def add_sub_category(self, sub_category):
        self.subcategories.append(sub_category)
