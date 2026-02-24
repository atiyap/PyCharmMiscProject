def calculate_bill(item_name, price, tax_percentage = 5):
    name = 'Item is', item_name
    item_price = 'price is', price
    tax_percentage = 'tax_percentage is', tax_percentage
    return name, item_price, tax_percentage
print(calculate_bill('Macbook', 2000))
print(calculate_bill('Lenovo', 500, 13))
