"""Write a program that:

Takes a sorted list of integers and a target as input.

Uses binary search to find if the target exists.

Prints "Found" if present, otherwise "Not Found".

Example:

Input: [5, 10, 15, 20, 25], target = 15
Output: Found"""

def binary_search(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return "Found"
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


arr = [5, 10, 15, 20, 25]
result = binary_search(arr,15)
print(result)