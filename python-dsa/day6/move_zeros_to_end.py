#Move all 0s to the end of the array while maintaining the relative order of non-zero elements.
# ✅ Move zeros to the end
# ✅ Keep the relative order of non-zero elements
# ✅ Do it in-place (modify the original array, don't create a new one)

# def moves_zeros_to_end(array):
#     for i in range(len(array)):
#         if array[i] == 0:
#             for j in range(i+1,len(array)):
#                     if array[j] != 0:
#                         array[i], array[j] = array[j], array[i]
#                         break
#     return array
def moves_zeros_to_end(array):
    non_zero = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[non_zero], array[i] = array[i], array[non_zero]
            non_zero += 1
    return array

arr = [1,0,5,3,0,5,2,8,4,-1,9,0]
result = moves_zeros_to_end(arr)
print(f"After moving {result}")
#time complexity O(n) and space complexity O(1)