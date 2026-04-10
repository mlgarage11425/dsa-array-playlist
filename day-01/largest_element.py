# Problem: Find Largest Element in Array
# input = [2, 5, 6, 3, 0]
# output = 6
# Approach: Basic Traversal
# Time Complexity: O(n)
# Space Complexity: O(1)

def large_element(arr):
    large = arr[0]
    for x in arr:
        if x > large:
            large = x
    return large

# Test
print(large_element([2, 5, 6, 3, 0]))