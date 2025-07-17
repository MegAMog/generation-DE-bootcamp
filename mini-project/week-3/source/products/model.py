from paths import product_file

# Load data from product file into list
original_products = []

try:
    with open(product_file, "r") as file:
        for line in file:
            original_products. append(line.strip())
except:
    #Create empty file if it doesn't exist.
    with open(product_file, 'w') as file:
        file.write('')