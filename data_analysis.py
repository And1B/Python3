import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visits_cart = visits.merge(cart, how="left")
len_visits = len(visits_cart)
len_no_visits_cart = len(visits_cart[visits_cart.cart_time.isnull()])
percentage_no_cart = float(len_no_visits_cart) / float(len_visits)
print("Percentage of people not placing a product into the cart:", percentage_no_cart * 100, "%")

cart_checkout = cart.merge(checkout, how="left")
len_cart_time = len(cart_checkout[cart_checkout.cart_time.notnull()])
len_no_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
percentage_cart_no_checkout = float(len_no_checkout) / float(len_cart_time)
print("Percentage of people placing product to cart and not going to checkout:", percentage_cart_no_checkout * 100, "%")

all_data = visits.merge(cart, how="left")\
                 .merge(checkout, how="left")\
                 .merge(purchase, how="left")
len_cart_time = len(all_data[all_data.cart_time.notnull()])
cart_data = all_data[all_data.cart_time.notnull()]
#print("All Data: ", len(all_data))
#print("Cart_Amount: ", len_cart_time)
checkout_data = cart_data[cart_data.checkout_time.notnull()]
len_checkout = len(checkout_data[checkout_data.checkout_time.notnull()])
#print("Checkout: ", len_checkout)
len_no_purchase = len(checkout_data[checkout_data.purchase_time.isnull()])
#print("Amount no purchase: ", len_no_purchase)
percentage_checkout_no_purchase = float(len_no_purchase) / float(len_checkout)
print("Percentage of people in checkout and not buying the product:", percentage_checkout_no_purchase * 100, "%")

all_data["time_until_purchase"] = all_data.purchase_time - all_data.visit_time
average_time = all_data.time_until_purchase.mean()
print(average_time)
