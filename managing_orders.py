tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': ['Orange Juice', 'Apple Juice'],
      'food_items': ['Pancakes'],
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)
    print('Total Amount:', total)
#calculate_price_per_person(534,20.0,5)

def remove_table(table_number):
  tables[table_number] = {}

def remove_items(table_number, item):
  drink_list = tables[table_number]['order']['drinks']
  food_list = tables[table_number]['order']['food_items']
  if item in drink_list:
    drink_list.remove(item)
  elif item in food_list:
    food_list.remove(item) 
  else:
    print("This order has not been added yet.")



assign_table(2, 'Arwa', True)
print(tables)
