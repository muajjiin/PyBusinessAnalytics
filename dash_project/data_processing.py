import pandas as pd


def load_data(file_path="Dummy_Retail_Data.xlsx"):
    customers = pd.read_excel(file_path, sheet_name="Customers")
    products = pd.read_excel(file_path, sheet_name="Products")
    orders = pd.read_excel(file_path, sheet_name="Orders")
    inventory = pd.read_excel(file_path, sheet_name="Inventory")

    # Merge orders with products and customers
    orders_products = orders.merge(products, on="Product_ID")
    orders_products_customers = orders_products.merge(customers, on="Customer_ID")

    # Add Revenue column
    orders_products_customers['Revenue'] = orders_products_customers['Quantity'] * orders_products_customers[
        'Unit_Price']

    # Add Month column for monthly analysis
    orders_products_customers['Order_Month'] = pd.to_datetime(orders_products_customers['Order_Date']).dt.to_period(
        'M').dt.to_timestamp()

    return customers, products, orders, inventory, orders_products_customers
