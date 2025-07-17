import os

#Find absolute path for current py-file
abs_path_current_file=os.path.abspath(__file__)

#Get the root directory
root_dir=os.path.dirname(os.path.dirname(abs_path_current_file))

#Get project directory
project_dir=os.path.dirname(os.path.dirname(root_dir))


#DATA
#Path to data directory
data_dir=os.path.join(root_dir, "data")

#Specifie files
product_file=os.path.join(data_dir, "products.csv")
courier_file=os.path.join(data_dir, "couriers.csv")
order_file=os.path.join(data_dir, "orders.csv")


#Environment
#Go 3 levels up from this file to .env
env_path = os.path.join(project_dir,'.env')
print(env_path)