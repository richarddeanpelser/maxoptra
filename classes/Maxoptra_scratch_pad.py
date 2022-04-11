from DiskReader import DiskReader as dr
from Maxoptra import MaxAPI as maxoptra
from Orders import Order
csv_data = dr.import_csv('csvdata/MaxOptra_Collections_20032022.csv')

max = maxoptra()
json_data = max.get(max.tags.orders())
ref_numbers = []
dummy_numbers = [
    '1000-180322-50474-STD',
    '1000-195686-56930-STD',
    '1000-237050-73026-STD',
    '1000-276820-87403-1000',
    '1000-302813-99436-1000'
]

# print(max.exists('1000-180322-50474-STD',ref_numbers))


dataset = Order().import_orders(csv_data)
print(dataset)
    

# for index in orders:
#     print(order.reference_number)
#     ref_numbers.append(order.reference_number)
#     print(ref_numbers)
#     ref_numbers.append(index['reference_number'])

# print(ref_numbers)
# json_data = max.get(max.tags.orders())  
# status = max.post(max.tags.orders(),json_data[0])
# print(status)
# print(json_data)

### TO DO ####
# Make dummy dataset containing reference numbers and only dumps csv orders 
# that don't exist in the reference numbers dataset
 