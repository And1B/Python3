from collections import deque, namedtuple

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

split_prices = deque()

for item in overstock_items:
  if item[1] > 20.00:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)

ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

bundles = list()
item_list = list()
while len(split_prices) >= 5:
  price = 0
  items_list = list()
  for i in range(3):
    item_list.append(split_prices.pop())
  for i in range(2):
    item_list.append(split_prices.popleft())
  for item in item_list:
    price += item[1]
    items_list.append(item[0])
  bundles.append(ClothesBundle(bundle_items=str(items_list), bundle_price=price))
  items_list.clear()
  item_list.clear()
promoted_bundles = list()
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)
print(promoted_bundles)
