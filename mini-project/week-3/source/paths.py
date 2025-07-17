import os

#Find absolute path for current py-file
abs_path_current_file=os.path.abspath(__file__)

#Get the root directory
root_dir=os.path.dirname(os.path.dirname(abs_path_current_file))
#Path to data directory
data_dir=os.path.join(root_dir, "data")

#Specifie files
product_file=os.path.join(data_dir, "products.txt")
courier_file=os.path.join(data_dir, "couriers.txt")