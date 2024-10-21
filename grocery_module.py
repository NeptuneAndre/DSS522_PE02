# grocery_module.py

def delivery_info(customer_name, items_dict, **kwargs):
    """
    Accepts customer name, a dictionary of items (item: quantity), and optional delivery address and time.
    """
    print(f"Customer: {customer_name}")
    
    # Print items and their quantities
    if items_dict:
        print("Items to deliver:")
        for item, quantity in items_dict.items():
            print(f" - {item}: {quantity}")
    else:
        print("No items to deliver.")
    
    # Handle additional details like address and delivery time
    address = kwargs.get('address', 'No address provided')
    delivery_time = kwargs.get('delivery_time', 'same-day')
    
    print(f"Delivery address: {address}")
    print(f"Delivery time: {delivery_time}")
