n = int(input('Enter Number of Items: '))

fruits = []
colors = []
quantities = []
prices = []

for i in range(n):
    fruit, color, quantity, price = input().split()

    fruits.append(fruit)
    colors.append(color)
    quantities.append(int(quantity))
    prices.append(float(price))

color_dict = {}

for color in colors:
    color_dict[color] = color_dict.get(color, 0) + 1

avg_quantity = sum(quantities) / n
avg_price = sum(prices) / n

print(fruits)
print(colors)
print(quantities, prices)
print(color_dict)
print(f"avg quantity:{avg_quantity:.2f}")
print(f"avg price:{avg_price:.2f}")

"""
Output:
        Enter Number of Items: 3
        Apple Red 10 50.5
        Banana Yellow 20 30.0
        Orange Orange 15 40.0
        ['Apple', 'Banana', 'Orange']
        ['Red', 'Yellow', 'Orange']
        [10, 20, 15] [50.5, 30.0, 40.0]
        {'Red': 1, 'Yellow': 1, 'Orange': 1}
        avg quantity:15.00
        avg price:40.17
"""