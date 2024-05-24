import itertools

# Step 2: Define the list of numbers
numbers = [3, 2, 2, 2, 3]
# numbers = [1, 2, 3, 2, 2, 3, 4, 2]

# Step 3: Generate all combinations of three numbers
combinations = itertools.combinations(numbers, 3)

# Step 4: Generate permutations for each combination
unique_permutations = set()
for combo in combinations:
    for perm in itertools.permutations(combo):
        number = int(''.join(map(str, perm)))
        unique_permutations.add(number)

# Convert the set to a sorted list
unique_numbers = sorted(unique_permutations)

# Function to check if two numbers differ in exactly one digit
def differ_by_one_place(num1, num2):
    str1, str2 = str(num1), str(num2)
    if len(str1) != len(str2):
        return False
    differences = sum(1 for a, b in zip(str1, str2) if a != b)
    return differences == 1

# Step 6: Compare pairs of numbers ensuring each number is used only once
used_numbers = set()
differing_pairs = []
for i, num1 in enumerate(unique_numbers):
    if num1 in used_numbers:
        continue
    for j, num2 in enumerate(unique_numbers[i+1:], start=i+1):
        if num2 in used_numbers:
            continue
        if differ_by_one_place(num1, num2):
            differing_pairs.append((num1, num2))
            used_numbers.add(num1)
            used_numbers.add(num2)
            break

# Print the pairs
for pair in differing_pairs:
    print(pair)
