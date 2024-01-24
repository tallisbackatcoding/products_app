import random

from v1.category.models import Category
from v1.product.models import Product
from v1.tag.models import Tag
from v1.product_has_tag.models import ProductHasTag

# Mock data

category_names = ["Console", "Phone", "Laptop", "Tablet", "Camera", "Headphones", "Smartwatch", "TV", "Printer", "Speaker"]
tag_names = ["Big Screen", "Portable", "Wireless", "4K", "Bluetooth", "Long Battery Life", "Touchscreen", "Waterproof", "Fast Charging", "High Resolution", "Lightweight", "Noise Cancelling", "VR Ready", "Voice Control", "Eco-Friendly"]
product_names = [
    "iPhone 13", "Galaxy S21", "OnePlus 9", "Pixel 5", "Moto G Power",
    "MacBook Pro", "Dell XPS 13", "HP Spectre x360", "Lenovo Yoga 9i", "Surface Laptop 4",
    "iPad Pro", "Samsung Galaxy Tab S7", "Amazon Fire HD 10", "Microsoft Surface Go", "Lenovo Tab P11",
    "Nikon D3500", "Canon EOS Rebel T7", "Sony Alpha A6000", "Fujifilm X-T4", "Olympus OM-D E-M10 Mark IV",
    "Sony WH-1000XM4", "Bose QuietComfort 35 II", "Sennheiser HD 450BT", "Apple AirPods Max", "Jabra Elite 85h",
    "Apple Watch Series 6", "Samsung Galaxy Watch 3", "Fitbit Versa 3", "Garmin Forerunner 245", "Fossil Gen 5",
    "Samsung QLED TV", "LG OLED TV", "Sony Bravia", "TCL 6-Series", "Vizio P-Series Quantum",
    "HP OfficeJet Pro", "Canon PIXMA", "Epson EcoTank", "Brother MFC", "Lexmark MC2535adwe",
    "JBL Flip 5", "Sonos One", "Bose SoundLink Revolve", "Marshall Emberton", "Ultimate Ears Boom 3",
    "PlayStation 5", "Xbox Series X", "Nintendo Switch", "Oculus Quest 2", "Sega Genesis Mini"
]
product_to_category_map = {
    "iPhone 13": "Phone", "Galaxy S21": "Phone", "OnePlus 9": "Phone", "Pixel 5": "Phone", "Moto G Power": "Phone",
    "MacBook Pro": "Laptop", "Dell XPS 13": "Laptop", "HP Spectre x360": "Laptop", "Lenovo Yoga 9i": "Laptop", "Surface Laptop 4": "Laptop",
    "iPad Pro": "Tablet", "Samsung Galaxy Tab S7": "Tablet", "Amazon Fire HD 10": "Tablet", "Microsoft Surface Go": "Tablet", "Lenovo Tab P11": "Tablet",
    "Nikon D3500": "Camera", "Canon EOS Rebel T7": "Camera", "Sony Alpha A6000": "Camera", "Fujifilm X-T4": "Camera", "Olympus OM-D E-M10 Mark IV": "Camera",
    "Sony WH-1000XM4": "Headphones", "Bose QuietComfort 35 II": "Headphones", "Sennheiser HD 450BT": "Headphones", "Apple AirPods Max": "Headphones", "Jabra Elite 85h": "Headphones",
    "Apple Watch Series 6": "Smartwatch", "Samsung Galaxy Watch 3": "Smartwatch", "Fitbit Versa 3": "Smartwatch", "Garmin Forerunner 245": "Smartwatch", "Fossil Gen 5": "Smartwatch",
    "Samsung QLED TV": "TV", "LG OLED TV": "TV", "Sony Bravia": "TV", "TCL 6-Series": "TV", "Vizio P-Series Quantum": "TV",
    "HP OfficeJet Pro": "Printer", "Canon PIXMA": "Printer", "Epson EcoTank": "Printer", "Brother MFC": "Printer", "Lexmark MC2535adwe": "Printer",
    "JBL Flip 5": "Speaker", "Sonos One": "Speaker", "Bose SoundLink Revolve": "Speaker", "Marshall Emberton": "Speaker", "Ultimate Ears Boom 3": "Speaker",
    "PlayStation 5": "Console", "Xbox Series X": "Console", "Nintendo Switch": "Console", "Oculus Quest 2": "Console", "Sega Genesis Mini": "Console"
}

tags_for_categories = {
    "Phone": ["Touchscreen", "Portable", "Long Battery Life", "Fast Charging", "4G", "5G"],
    "Laptop": ["Portable", "Long Battery Life", "High Resolution", "Wireless", "Bluetooth"],
    "Tablet": ["Touchscreen", "Portable", "Lightweight", "Long Battery Life", "High Resolution"],
    "Camera": ["High Resolution", "Portable", "4K", "Wireless"],
    "Headphones": ["Wireless", "Bluetooth", "Noise Cancelling", "Long Battery Life", "Portable"],
    "Smartwatch": ["Touchscreen", "Bluetooth", "Waterproof", "Long Battery Life", "Portable"],
    "TV": ["4K", "High Resolution", "Bluetooth", "Smart TV", "Voice Control"],
    "Printer": ["Wireless", "Bluetooth", "High Resolution", "Eco-Friendly"],
    "Speaker": ["Portable", "Wireless", "Bluetooth", "High Resolution", "Eco-Friendly"],
    "Console": ["Wireless", "Bluetooth", "4K", "High Resolution", "VR Ready"]
}

descriptions = [
    "High-quality and reliable", "Innovative features and design", "User-friendly and efficient",
    "Compact and versatile", "Exceptional performance", "Elegant and sleek", "Advanced technology",
    "Durable and long-lasting", "Cost-effective and valuable", "Eco-friendly and sustainable"
]

for name in category_names:
    Category.objects.get_or_create(name=name)

# Create Tags
for name in tag_names:
    Tag.objects.get_or_create(name=name)

for name in category_names:
    Category.objects.get_or_create(name=name)

# Create Products
for product_name, category_name in product_to_category_map.items():
    category = Category.objects.get(name=category_name)
    description = random.choice(descriptions)
    product, created = Product.objects.get_or_create(name=product_name, category=category, defaults={'description': description})
    if created:
        tag_names = tags_for_categories.get(category.name, [])
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            ProductHasTag.objects.get_or_create(product=product, tag=tag)

print("Mock data created successfully!")