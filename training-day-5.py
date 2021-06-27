#there is no point statement so it will not print anything
items_and_amount = {"banana": 4,
                    "milk": 2,
                    "soda bottle": 1}
print(items_and_amount)

fruit_or_vegtable = {"apple": "fruit",
                    "carrot": "vegtable",
                     "lemon": "fruit",
                     "lettuce": "vegtable",
                     "bluebary": "fruit",
                     "grape": "fruit",}

#Chosses one things from the dictionary
foods = {"apple": "fruit",
                    "carrot": "vegtable",
                     "lemon": "fruit",
                     "lettuce": "vegtable",
                     "bluebary": "fruit",
                     "grape": "fruit",}

print(foods["apple"])

#modifying the dictionary
foods = {"apple": "fruit",
                    "carrot": "vegtable",
                     "lemon": "fruit",
                     "lettuce": "vegtable",
                     "bluebary": "fruit",
                     "grape": "fruit",}

print(foods["apple"])
foods["tamato"] = "fruit"

print(foods["tamato"])

foods["bread"] = "grain"

print(foods["bread"])
#pop will return the value back
foods.pop("lettuce")

item_and_amount = {"banana": 4,
                   "milk": 2,
                   "soda bottle": 1,
                   "orange juice": 2}
print(list(items_and_amount.keys())[list(items_and_amount.values()).index(2)])

foods.update(item_and_amount)

print(foods)

x = 5
y = x
y += 1

print("x is", x)
print("y is", y)

x = [5,10]

y = list(x)

y[0] = 6

print("x is", x)
print("y is", y)
