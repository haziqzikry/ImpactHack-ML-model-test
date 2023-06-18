import json
from faker import Faker
import random
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()

# Generate sample data
data = []
start_date = datetime.now() - timedelta(days=300)  # Start date for generating past dates
for _ in range(300):  # Generate 300 data points
    product_type = random.choice(['Electronics', 'Clothing', 'Home', 'Sports'])
    sku = fake.random_int(min=1000, max=9999)
    price = round(random.uniform(10, 100), 2)
    availability = random.choice(['In Stock', 'Out of Stock'])
    num_products_sold = random.randint(0, 100)
    revenue_generated = price * num_products_sold
    customer_demographics = random.choice(['Male', 'Female', 'Other'])
    stock_levels = random.randint(0, 1000)
    lead_times = random.randint(1, 7)
    order_quantities = random.randint(1, 10)
    shipping_times = random.randint(1, 5)
    shipping_carriers = random.choice(['FedEx', 'UPS', 'DHL'])
    shipping_costs = round(random.uniform(5, 20), 2)
    
    # Generate multiple order details for SKU 7841
    order_dates = []
    shipment_dates = []
    received_dates = []
    if sku == 7841:
        for _ in range(random.randint(1, 5)):
            order_date = fake.date_between(start_date=start_date, end_date='today')
            shipment_date = order_date + timedelta(days=random.randint(1, 7))
            received_date = shipment_date + timedelta(days=random.randint(1, 5))
            
            order_dates.append(order_date.strftime('%Y-%m-%d'))
            shipment_dates.append(shipment_date.strftime('%Y-%m-%d'))
            received_dates.append(received_date.strftime('%Y-%m-%d'))
    
    # Create a data point dictionary
    data_point = {
        'Product type': product_type,
        'SKU': sku,
        'Price': price,
        'Availability': availability,
        'Number of products sold': num_products_sold,
        'Revenue generated': revenue_generated,
        'Customer demographics': customer_demographics,
        'Stock levels': stock_levels,
        'Lead times': lead_times,
        'Order quantities': order_quantities,
        'Shipping times': shipping_times,
        'Shipping carriers': shipping_carriers,
        'Shipping costs': shipping_costs,
        'Order date': order_dates,
        'Shipment date': shipment_dates,
        'Received date': received_dates
    }
    
    data.append(data_point)

# Save data to a JSON file
with open('inventory_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
