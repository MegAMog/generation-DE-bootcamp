from paths import courier_file

# Load data from courier file into courier list
original_couriers=[]

try:
    with open(courier_file, "r") as file:
        for line in file:
            original_couriers.append(line.strip())
except:
    #Create empty file if it doesn't exist.
    with open(courier_file, 'w') as file:
        file.write('')