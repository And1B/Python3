clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)

coat_cost = new_coat.price

updated_clothes_data = list()
for tuple_item in clothes:
  updated_clothes_data.append(ClothingItem(tuple_item[0], tuple_item[1], tuple_item[2], tuple_item[3]))
print(updated_clothes_data)
