arr = [10,20,30,99,40,100,50]
# arr.sort()        #time complexity O(n)
# arr_len = len(arr)
# print("max:",arr[arr_len-1])
# print("min:",arr[0])
#same as above
max_ele = arr[0]
min_ele = arr[0]
for i in arr:                           #time complexity O(n) space complexity O(1)
    if i > max_ele:
        max_ele = i
    if i < min_ele:
        min_ele = i
print(max_ele,min_ele)