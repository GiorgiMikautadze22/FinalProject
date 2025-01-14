from Module7.task_5_data_classes.app import SessionLocal, Category

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

electronics = CategoryRepository()
electronics.create_category("Electronics")