categories = []
products = []
stocks = []

num_categories = 3
num_products = 2

for i in range(num_categories):
    category = input(f"Enter Category {i + 1} Name: ")
    categories.append(category)

    product_list = []
    stock_list = []

    for j in range(num_products):
        product = input(f"Enter Product {j + 1} for {category}:")
        stock = int(input(f"Enter Stock for {product}: "))

        product_list.append(product)
        stock_list.append(stock)

    products.append(product_list)
    stocks.append(stock_list)

print("\n------ Inventory Report ------")

for i in range(num_categories):
    print(f"\Category: {categories[i]}")
    for j in range(num_products):
        print(f"{products[i][j]}: {stocks[i][j]} units")