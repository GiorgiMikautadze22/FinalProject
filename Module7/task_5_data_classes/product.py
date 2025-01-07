class ProductModel:
    def __init__(self, model):
        self.model = model

class Product:
    def __init__(self, name, category, model = None):
        self.name = name
        self.category = category
        self.model = model

        category.add_product(name)