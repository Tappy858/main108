def products_test():
    products = [
        {
            "title": "Smartphone",
            "image": "smartphone.jpg",
            "price": 299.99,
            "category": "Electronics",
        },
        {
            "title": "Running Shoes",
            "image": "running_shoes.jpg",
            "price": 89.99,
            "category": "Footwear",
        },
        {
            "title": "Backpack",
            "image": "backpack.jpg",
            "price": 49.99,
            "category": "Accessories",
        },
        {
            "title": "Coffee Maker",
            "image": "coffee_maker.jpg",
            "price": 119.99,
            "category": "Home Appliances",
        },
        {
            "title": "Wireless Headphones",
            "image": "wireless_headphones.jpg",
            "price": 159.99,
            "category": "Electronics",
        },
        {
            "title": "Fitness Tracker",
            "image": "fitness_tracker.jpg",
            "price": 59.99,
            "category": "Wearables",
        },
        {
            "title": "Digital Camera",
            "image": "digital_camera.jpg",
            "price": 349.99,
            "category": "Electronics",
        },
        {
            "title": "Yoga Mat",
            "image": "yoga_mat.jpg",
            "price": 25.99,
            "category": "Fitness",
        },
        {
            "title": "Novel - 'Mystery of the Old Manor'",
            "image": "novel.jpg",
            "price": 14.99,
            "category": "Books",
        },
        {
            "title": "Portable Charger",
            "image": "portable_charger.jpg",
            "price": 39.99,
            "category": "Electronics",
        },
    ]
    
    # A) Print title and $ Price
    # B) What is the total of Electronics?
    total = 0

    # C) How many Electronics products exist in the list?
    count = 0
    
    # D) find the cheapest
    # E) list of unique categories (list only once)

    for product in products:
        print(f"{product['title']} ${product['price']}")
        if product["category"] == "Electronics":
            total += product["price"]
            count += 1

    print(f"Total price of Electronics: ${total}")
    print(f"Number of Electronic products: {count}")

    
# fn call
products_test()
