import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define data parameters
n_customers = 2500

# Customer demographics
genders = ['Male', 'Female', 'Other']
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
locations = ['California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 
             'Ohio', 'Georgia', 'North Carolina', 'Michigan', 'New Jersey', 'Virginia']

# Product categories
categories = ['Clothing', 'Electronics', 'Footwear', 'Accessories', 'Home & Garden', 
              'Sports & Outdoors', 'Beauty & Personal Care', 'Books & Media', 'Toys & Games']

# Purchase items
items = {
    'Clothing': ['Shirt', 'Pants', 'Dress', 'Jacket', 'Sweater', 'Jeans', 'Blouse'],
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Tablet', 'Smartwatch', 'Camera'],
    'Footwear': ['Sneakers', 'Boots', 'Sandals', 'Heels', 'Running Shoes', 'Casual Shoes'],
    'Accessories': ['Watch', 'Handbag', 'Sunglasses', 'Jewelry', 'Belt', 'Wallet'],
    'Home & Garden': ['Furniture', 'Kitchenware', 'Decor', 'Bedding', 'Garden Tools'],
    'Sports & Outdoors': ['Fitness Equipment', 'Camping Gear', 'Sports Apparel', 'Bike'],
    'Beauty & Personal Care': ['Skincare', 'Makeup', 'Hair Care', 'Fragrance'],
    'Books & Media': ['Novel', 'Magazine', 'DVD', 'Music Album'],
    'Toys & Games': ['Board Game', 'Action Figure', 'Puzzle', 'Video Game']
}

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
subscription_status = ['Yes', 'No']
payment_methods = ['Credit Card', 'Cash', 'Debit Card', 'PayPal', 'Bank Transfer']
shipping_types = ['Standard', 'Express', 'Next Day Delivery', 'Free Shipping']
promo_codes = ['Yes', 'No']
frequency = ['Weekly', 'Bi-Weekly', 'Monthly', 'Quarterly', 'Annually']

# Generate data
data = []

for i in range(n_customers):
    customer_id = i + 1
    age = random.choice(age_groups)
    gender = np.random.choice(genders, p=[0.48, 0.48, 0.04])
    
    # Generate purchase data
    category = random.choice(categories)
    item = random.choice(items[category])
    
    # Price varies by category
    if category == 'Electronics':
        purchase_amount = np.random.normal(400, 200)
    elif category == 'Clothing':
        purchase_amount = np.random.normal(75, 30)
    elif category == 'Footwear':
        purchase_amount = np.random.normal(120, 50)
    elif category == 'Accessories':
        purchase_amount = np.random.normal(90, 40)
    elif category == 'Home & Garden':
        purchase_amount = np.random.normal(150, 80)
    elif category == 'Sports & Outdoors':
        purchase_amount = np.random.normal(110, 60)
    elif category == 'Beauty & Personal Care':
        purchase_amount = np.random.normal(45, 20)
    elif category == 'Books & Media':
        purchase_amount = np.random.normal(25, 10)
    else:  # Toys & Games
        purchase_amount = np.random.normal(35, 15)
    
    purchase_amount = max(10, purchase_amount)  # Minimum purchase amount
    
    # Other attributes
    location = random.choice(locations)
    size = random.choice(['XS', 'S', 'M', 'L', 'XL']) if category in ['Clothing', 'Footwear'] else 'N/A'
    color = random.choice(['Black', 'White', 'Blue', 'Red', 'Green', 'Gray', 'Brown']) if category in ['Clothing', 'Footwear', 'Accessories'] else 'N/A'
    season = random.choice(seasons)
    subscription = np.random.choice(subscription_status, p=[0.3, 0.7])
    payment_method = random.choice(payment_methods)
    shipping_type = random.choice(shipping_types)
    discount_applied = np.random.choice(promo_codes, p=[0.25, 0.75])
    promo_code_used = np.random.choice(promo_codes, p=[0.2, 0.8])
    previous_purchases = np.random.poisson(5) + 1
    review_rating = np.random.choice([3, 4, 5], p=[0.1, 0.3, 0.6])
    purchase_frequency = random.choice(frequency)
    
    data.append({
        'Customer ID': customer_id,
        'Age': age,
        'Gender': gender,
        'Item Purchased': item,
        'Category': category,
        'Purchase Amount (USD)': round(purchase_amount, 2),
        'Location': location,
        'Size': size,
        'Color': color,
        'Season': season,
        'Review Rating': review_rating,
        'Subscription Status': subscription,
        'Payment Method': payment_method,
        'Shipping Type': shipping_type,
        'Discount Applied': discount_applied,
        'Promo Code Used': promo_code_used,
        'Previous Purchases': previous_purchases,
        'Purchase Frequency': purchase_frequency
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/shopping_trends.csv', index=False)
print(f"Generated shopping trends dataset with {len(df)} records")
print(f"Dataset saved to data/shopping_trends.csv")
print("\nDataset preview:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")