# DONE: Create a class called recipe
class Recipe():
    # def __new__(cls) -> Self:
    #     pass
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        ("The " + self.dish + " has " + str(self.items) + \
            " and takes " + str(self.time) + " min to prepare")
        
pizza  = Recipe("Pizza", ["cheese", "bread", "tomato sauce"], 45)
pasta  = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.dish, pizza.items)
print(pasta.dish, pasta.items)

print(pizza.contents())