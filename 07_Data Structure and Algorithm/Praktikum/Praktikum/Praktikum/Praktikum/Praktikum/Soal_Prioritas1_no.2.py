def get_breads(breads, flour_stock):
    can_make = []
    for bread in breads:
        if bread["flour"] <= flour_stock:
            can_make.append(bread["name"])
            flour_stock -= bread["flour"]
    return can_make

bread1 = [
  {"name": "donut", "flour": 25},
  {"name": "mini puff", "flour": 15},
  {"name": "baguette", "flour": 75},
  {"name": "cupcake", "flour": 15},
]

bread2 = [
  {"name": "pancake", "flour": 15},
  {"name": "waffle", "flour": 25},
  {"name": "bagel", "flour": 15},
  {"name": "cupcake", "flour": 15},
  {"name": "choco chips", "flour": 10},
  {"name": "mini puff", "flour": 5},
  {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))  # ['donut', 'mini puff', 'cupcake']
print(get_breads(bread2, 75))  # ['pancake', 'waffle', 'bagel', 'cupcake', 'choco chips', 'mini puff']