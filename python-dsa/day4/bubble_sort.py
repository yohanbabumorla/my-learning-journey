def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


array = [3,5,8,6,2]
result = bubble_sort(array)
print(result)
#time O(n^2) space O(1)