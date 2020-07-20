toppings = ["pepperoni", "pineapple",
            "cheese", "sausage", "olives",
            "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)



print(f"We sell {num_pizzas} different kinds of pizza!")


#get_num_pizzas()

pizzas = list(zip(prices, toppings))
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(pizzas)
print(cheapest_pizza)
print(priciest_pizza)
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)