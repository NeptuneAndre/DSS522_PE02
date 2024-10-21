# main.py

# Import the delivery_info function from grocery_module
from grocery_module import delivery_info

# Define the grocery items and quantities using a dictionary
items_to_deliver = {
    "Apples": "2 kg",
    "Milk": "1 liter",
    "Bread": "1 loaf"
}

# Call the delivery_info function with customer details
delivery_info(
    "John Doe",  # Customer name
    items_to_deliver,  # Items to deliver (dictionary)
    address="123 Main Street, Cityville",  # Optional address
    delivery_time="next-day"  # Optional delivery time
)
