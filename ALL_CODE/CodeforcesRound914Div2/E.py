def custom_key(element):
    # You can adjust this function based on your specific requirement
    # For example, using the absolute difference between each element and a reference value.
    reference_value = 0
    return abs(element - reference_value)

# Example array
my_array = [10, 3, 8, 1, 6]

# Sort the array based on the custom key function
sorted_array = sorted(my_array, key=custom_key)

# Print the sorted array
print(sorted_array)