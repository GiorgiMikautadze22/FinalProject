from Module7.task_5_data_classes.app import SessionLocal, Category, Product, ProductModel
from sqlalchemy import select


class CategoryRepository:
    def create_category(self, category, parent_id = None):
        session = SessionLocal()
        category = Category(
            name=category,
            parent_category_id=parent_id
        )
        session.add(category)
        session.commit()
        session.close()
        print("New Category has been created")

    def get_category(self, name):
        session = SessionLocal()
        category = session.execute(select(Category).where(Category.name == name)).scalar_one_or_none()
        session.close()
        return category

    def get_all_categories(self):
        session = SessionLocal()
        categories = session.execute(select(Category)).all().scalars()
        session.close()
        return categories


class ProductModelRepository:
    def create_model(self, name, description,):
        session = SessionLocal()
        model = ProductModel(
            name=name,
            catalog_description=description
        )
        session.add(model)
        session.commit()
        session.close()
        print("New Model has been created")

class ProductRepository:
    def create_product(self, name, product_number, color, category, start, end, discount_date, product_model = None):
        session = SessionLocal()
        selected_category = session.execute(select(Category).where(Category.name == category)).scalar_one_or_none()

        if product_model:
            product_model = session.execute(select(ProductModel).where(ProductModel.name == product_model)).scalar_one_or_none().id

        product = Product(
            name=name,
            product_number=product_number,
            color=color,
            category_id=selected_category.id,
            sell_start_date=start,
            sell_end_date=end,
            discount_date=discount_date,
            product_model_id=product_model
        )

        session.add(product)
        session.commit()
        session.close()
        print("New Product has been created")


electronics = CategoryRepository()
# electronics.create_category("Electronics")
#
# model = ProductModelRepository()
# model.create_model("Iphone", "Apple Phones")
#
# product = ProductRepository()
# product.create_product("Iphone", 22, "red", "Electronics", "22 august", "30 august", "25 august")
