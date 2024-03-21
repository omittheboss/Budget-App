from budget import Category, create_spend_chart

# Example usage
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

clothing.deposit(500, "initial deposit")
clothing.transfer(50, food)

auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")
auto.withdraw(25, "oil change")

print(food)
print(clothing)
print(auto)

categories = [food, clothing, auto]
chart = create_spend_chart(categories)
print(chart)
