def count_array_element(array,target):
    target_count = 0
    for i in array:
        if i == target:
            target_count += 1
    return target,target_count


arr = [1,2,3,2,4,5,6,7,4,6,8,7]
print(f"\narray:{arr}\n")
result1,target2 = count_array_element(arr,7)
print(f"the count of {result1} in array  is {target2}")

"""time complexity is O(n) and space complexity is O(1)"""