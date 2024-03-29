class Customer:
 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number


class CustomerWrap(Customer):
 
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)


customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()

------------------------------------------------------------------------------------------------------

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

from collections import UserDict

class OrderProcessingDict(UserDict):
  def clean_orders(self):
    to_delete = list()
    for key, value in self.data.items():
      if value['order_status'] == 'complete':
        to_delete.append(key)
    for item in to_delete:
      del self.data[item]
process_dict = OrderProcessingDict(data)
print(process_dict)
print(process_dict.clean_orders())

------------------------------------------------------------------------------------------------------

from collections import UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

class ListSorter(UserList):
  def append(self, value):
    super().append(value)
    self.data.sort()
    
sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)    
