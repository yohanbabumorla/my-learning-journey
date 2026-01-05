def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]   # creating a temp variable and initializing with first element in unsorted array
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]         #swap the value in the sorted with unsorted if the value in sorted > unsorted value[which is k]
            j -= 1    #check the condition is true from left to right side of sorted array #j is decreased
        arr[j+1] = key #initialize the temp val in j+1
    return arr

array = [5,4,10,1,6,2]
result = insertion_sort(array)
print(result)
