from Module7.task_5_data_classes.app import SessionLocal, Category, Product, ProductModel, Customer, Address, Order, OrderDetails
from sqlalchemy import select, update, delete


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
        categories = session.execute(select(Category)).scalars().all()
        session.close()
        return categories

    def update_category(self, category_id, name=None, parent_id=None):
        session = SessionLocal()

        category = session.execute(select(Category).where(Category.id == category_id)).scalar_one_or_none()
        if name:
            category.name = name
        if parent_id:
            category.parent_category_id = parent_id

        session.commit()
        session.close()
        print("Category has been updated")

    def delete_category(self, category_id):
        session = SessionLocal()
        category = session.execute(select(Category).where(Category.id == category_id)).scalar_one_or_none()
        session.delete(category)
        session.commit()
        session.close()
        print("Category has been deleted")


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

    def get_model(self, id):
        session = SessionLocal()
        model = session.execute(select(ProductModel).where(ProductModel.id == id)).scalar_one_or_none()
        session.close()
        return model

    def get_all_categories(self):
        session = SessionLocal()
        categories = session.execute(select(ProductModel)).scalars().all()
        session.close()
        return categories

    def delete_model(self, model_id):
        session = SessionLocal()
        model = session.execute(select(ProductModel).where(ProductModel.id == model_id)).scalar_one_or_none()
        session.delete(model)
        session.commit()
        session.close()
        print("Category has been deleted")

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

    def get_product_by_id(self, product_id: int):
        session = SessionLocal()
        return session.get(Product, product_id)

    def get_all_products(self):
        session = SessionLocal()
        return session.execute(select(Product)).scalars().all()

    def update_product(self, product_id: int, **kwargs):
        session = SessionLocal()
        session.execute(
            update(Product)
            .where(Product.id == product_id)
            .values(**kwargs)
        )
        session.commit()

    def delete_product(self, product_id: int):
        session = SessionLocal()
        session.execute(
            delete(Product)
            .where(Product.id == product_id)
        )
        session.commit()

class CustomerRepository:
    def create_customer(self, name_style: int, first_name: str, middle_name: str, last_name: str, sales_person: str, email_address: str, phone: str, title: str = None, suffix: str = None,company_name: str = None):

        session = SessionLocal()
        new_customer = Customer(
            name_style=name_style,
            title=title,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            suffix=suffix,
            company_name=company_name,
            sales_person=sales_person,
            email_address=email_address,
            phone=phone
        )
        session.add(new_customer)
        session.commit()
        session.refresh(new_customer)
        return new_customer

    def get_customer_by_id(self, customer_id: int):
        session = SessionLocal()
        return session.get(Customer, customer_id)

    def get_all_customers(self):
        session = SessionLocal()
        return session.execute(select(Customer)).scalars().all()

    def update_customer(self, customer_id: int, **kwargs):
        session = SessionLocal()
        session.execute(
            update(Customer)
            .where(Customer.id == customer_id)
            .values(**kwargs)
        )
        session.commit()

    def delete_customer(self, customer_id: int):
        session = SessionLocal()
        session.execute(
            delete(Customer)
            .where(Customer.id == customer_id)
        )
        session.commit()

class AddressRepository:

    def create_address(self, address_line_1: str, city: str, state: str, postal_code: int, country: str,
                       customer_id: int, address_line_2: str = None):
        session = SessionLocal()
        new_address = Address(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            customer_id=customer_id
        )
        session.add(new_address)
        session.commit()
        session.refresh(new_address)
        return new_address

    def get_address_by_id(self, address_id: int):
        session = SessionLocal()

        return session.get(Address, address_id)

    def get_all_addresses(self):
        session = SessionLocal()

        return session.execute(select(Address)).scalars().all()

    def get_addresses_by_customer_id(self, customer_id: int):
        session = SessionLocal()

        return session.execute(
            select(Address).where(Address.customer_id == customer_id)
        ).scalars().all()

    def update_address(self, address_id: int, **kwargs):
        session = SessionLocal()

        session.execute(
            update(Address)
            .where(Address.id == address_id)
            .values(**kwargs)
        )
        session.commit()

    def delete_address(self, address_id: int):
        session = SessionLocal()

        session.execute(
            delete(Address)
            .where(Address.id == address_id)
        )
        session.commit()

class OrderRepository:
    def create_order(
            self,
            order_number: int,
            order_date: str,
            ship_date: str,
            status: int,
            online_order_flag: int,
            purchase_order_number: int,
            account_number: int,
            customer_id: int,
            ship_address_id: int,
            bill_address_id: int,
            ship_method: str,
            credit_card_approval_code: int,
            sub_total: int,
            tax_amount: int,
            freight: int,
            total_due: int,
            comment: str,
            revision_number: int = None
    ):
        session = SessionLocal()

        new_order = Order(
            order_number=order_number,
            revision_number=revision_number,
            order_date=order_date,
            ship_date=ship_date,
            status=status,
            online_order_flag=online_order_flag,
            purchase_order_number=purchase_order_number,
            account_number=account_number,
            customer_id=customer_id,
            ship_address_id=ship_address_id,
            bill_address_id=bill_address_id,
            ship_method=ship_method,
            credit_card_approval_code=credit_card_approval_code,
            sub_total=sub_total,
            tax_amount=tax_amount,
            freight=freight,
            total_due=total_due,
            comment=comment,
        )
        session.add(new_order)
        session.commit()
        session.refresh(new_order)
        return new_order

    def get_order_by_id(self, order_id: int):
        session = SessionLocal()

        return session.get(Order, order_id)

    def get_all_orders(self):
        session = SessionLocal()

        return session.execute(select(Order)).scalars().all()

    def get_orders_by_customer_id(self, customer_id: int):
        session = SessionLocal()

        return session.execute(
            select(Order).where(Order.customer_id == customer_id)
        ).scalars().all()

    def update_order(self, order_id: int, **kwargs):
        session = SessionLocal()

        session.execute(
            update(Order)
            .where(Order.id == order_id)
            .values(**kwargs)
        )
        session.commit()

    def delete_order(self, order_id: int):
        session = SessionLocal()

        session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        session.commit()

class OrderDetailsRepository:
    def create_order_detail(
            self,
            order_id: int,
            order_quantity: int,
            product_id: int,
            unit_price: int,
            unit_price_discount: int,
            line_total: int
    ):
        session = SessionLocal()

        new_order_detail = OrderDetails(
            order_id=order_id,
            order_quantity=order_quantity,
            product_id=product_id,
            unit_price=unit_price,
            unit_price_discount=unit_price_discount,
            line_total=line_total,
        )
        session.add(new_order_detail)
        session.commit()
        session.refresh(new_order_detail)
        return new_order_detail

    def get_order_detail_by_id(self, order_detail_id: int):
        session = SessionLocal()

        return session.get(OrderDetails, order_detail_id)

    def get_order_details_by_order_id(self, order_id: int):
        session = SessionLocal()

        return session.execute(
            select(OrderDetails).where(OrderDetails.order_id == order_id)
        ).scalars().all()

    def update_order_detail(self, order_detail_id: int, **kwargs):
        session = SessionLocal()

        session.execute(
            update(OrderDetails)
            .where(OrderDetails.id == order_detail_id)
            .values(**kwargs)
        )
        session.commit()

    def delete_order_detail(self, order_detail_id: int):
        session = SessionLocal()

        session.execute(
            delete(OrderDetails)
            .where(OrderDetails.id == order_detail_id)
        )
        session.commit()
