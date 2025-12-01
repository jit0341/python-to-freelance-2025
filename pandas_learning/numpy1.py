# import numpy as np
# Create array of 5 numbers
import numpy as np 
arr = np.array([10, 20, 30, 40, 50])
print(arr)
print(type(arr))

# Set seed (makes random numbers same each time)

np.random.seed(42)

# Create 10 random numbers between 1 and 100
random_numbers = np.random.randint(1,100,10)
print(random_numbers)

np.random.seed(43)
random_numbers = np.random.randint(1, 100, 10)
print(random_numbers)

# Create list of products
products = ['Laptop', 'Phone', 'Tablet']

# Pick 10 random products (with repetition)
random_products = np.random.choice(products, 10)
print(random_products)

# Pick 5 random regions
regions = ['North', 'South', 'East', 'West']
random_regions = np.random.choice(regions, 5)
print(random_regions)

