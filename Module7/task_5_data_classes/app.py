import os

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    product_number: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String, nullable=False)
    # Relationship between category and product
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category",back_populates="products")

    # Relationship between product model and product
    product_model_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_models.id"), nullable=True)
    product_model: Mapped["ProductModel"] = relationship("ProductModel",back_populates="product")

    sell_start_date: Mapped[str] = mapped_column(String, nullable=False)
    sell_end_date: Mapped[str] = mapped_column(String, nullable=False)
    discount_date: Mapped[str] = mapped_column(String, nullable=False)

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    parent_category_id: Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    # Category can have many products
    products: Mapped[list["Product"]] = relationship("Product",back_populates="category")


# class Customer(Base):
#     __tablename__ = "customers"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name_style: Mapped[int] = mapped_column(Integer, nullable=False)
#     title: Mapped[str] = mapped_column(String, nullable=True)
#     first_name: Mapped[str] = mapped_column(String, nullable=False)
#     middle_name: Mapped[str] = mapped_column(String, nullable=False)
#     last_name: Mapped[str] = mapped_column(String, nullable=False)
#     suffix: Mapped[str] = mapped_column(String, nullable=True)
#     company_name: Mapped[str] = mapped_column(String, nullable=True)
#     sales_person: Mapped[str] = mapped_column(String, nullable=False)
#     email_address: Mapped[str] = mapped_column(String, nullable=False)
#     phone: Mapped[str] = mapped_column(String, nullable=False)
#
#     # Customer can have many addresses
#     customer_addresses: Mapped[list["Address"]] = relationship(secondary="customer_addresses")
#
#
# class Address(Base):
#     __tablename__ = "addresses"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     address_line_1: Mapped[str] = mapped_column(String(250), nullable=False)
#     address_line_2: Mapped[str] = mapped_column(String(250), nullable=True)
#     city: Mapped[str] = mapped_column(String, nullable=False)
#     state: Mapped[str] = mapped_column(String, nullable=False)
#     postal_code : Mapped[int]= mapped_column(Integer, nullable=False)
#     country: Mapped[str] = mapped_column(String, nullable=False)
#
#     # Relationship between customer and address
#     customer_address: Mapped[list["Customer"]] = relationship(secondary="customer_addresses",back_populates="last_name")
#
# class CustomerAddress(Base):
#     __tablename__ = "customer_addresses"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     customer_id: Mapped[int] = mapped_column(Integer,ForeignKey("customers.id"), nullable=False, primary_key=True)
#     address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"), nullable=False, primary_key=True)
#     address_type: Mapped[int] = mapped_column(String, nullable=False)
#
# class Order(Base):
#     __tablename__ = "orders"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_number: Mapped[int] = mapped_column(Integer, nullable=False)
#     revision_number: Mapped[int] = mapped_column(Integer, nullable=True)
#     order_date: Mapped[str] = mapped_column(String, nullable=False)
#     ship_date: Mapped[str] = mapped_column(String, nullable=False)
#     status: Mapped[int] = mapped_column(Integer, nullable=False)
#     online_order_flag: Mapped[int] = mapped_column(Integer, nullable=False)
#     purchase_order_number: Mapped[int] = mapped_column(Integer, nullable=False)
#     account_number: Mapped[int] = mapped_column(Integer, nullable=False)
#     customer_id: Mapped[int] = mapped_column(Integer,ForeignKey("customers.id"), nullable=False)
#     ship_address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"), nullable=False)
#     bill_address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"), nullable=False)
#     ship_method: Mapped[str] = mapped_column(String, nullable=False)
#     credit_card_approval_code: Mapped[int] = mapped_column(Integer, nullable=False)
#     sub_total: Mapped[int] = mapped_column(Integer, nullable=False)
#     tax_amount: Mapped[int] = mapped_column(Integer, nullable=False)
#     freight: Mapped[int] = mapped_column(Integer, nullable=False)
#     total_due: Mapped[int] = mapped_column(Integer, nullable=False)
#     comment: Mapped[str] = mapped_column(String, nullable=False)
#
# class OrderDetails(Base):
#     __tablename__ = "order_details"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"), nullable=False)
#     order_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
#     product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
#     unit_price: Mapped[int] = mapped_column(Integer, nullable=False)
#     unit_price_discount: Mapped[int] = mapped_column(Integer, nullable=False)
#     line_total: Mapped[int] = mapped_column(Integer, nullable=False)

class ProductModel(Base):
    __tablename__ = "product_models"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    catalog_description: Mapped[str] = mapped_column(String(250), nullable=False)
    product: Mapped[list["Product"]] = relationship("Product", back_populates="product_model")


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "final-project.db")
database_url = f"sqlite:///{db_path}"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


