import itertools

# Part 2: Possible Combinations

# Step 1: Define two sets with string elements
set1 = {'apple', 'banana', 'orange'}
set2 = {'car', 'bike'}

# Step 2: Generate all possible combinations of elements from both sets
combinations = list(itertools.product(set1, set2))

# Step 3: Output the combinations
print("All possible combinations:")
for combo in combinations:
    print(combo)

# Comment: 
# Real-world use case:
# Generating possible combinations is useful in product recommendation systems.
# For example, if an online store wants to recommend combinations of fruits and vehicles
# in a promotion or bundle, all possible combinations of the products can be generated
# and displayed to customers.
