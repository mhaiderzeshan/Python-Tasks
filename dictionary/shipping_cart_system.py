product_catalog = {
    "apple":  3.0,
    "banana": 1.5,
    "milk": 2.5,
    "bread": 2.0
}

cart = {
    "apple": 4,
    "banana": 6,
    "milk": 2,
    "bread": 3
}

discounts = {
    "apple": 10,  # 10% off
    "milk": 20  # 20% off
    # if no discount is there for the product, it means discount : 0%
}

final_bill = {}

for name, price in cart.items():
    price_of_product = product_catalog.get(name, 0)
    quantity = cart.get(name, 0)

    discount_price = (price_of_product * quantity) * (discounts.get(name, 0)/ 100)
    
    total_price = (price_of_product * quantity) - discount_price

    final_bill[name] = round(total_price, 2)

print(final_bill)
