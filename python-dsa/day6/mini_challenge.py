# Input: arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: maximum sum of subarray of size 4
def max_sum_subarray(array,k):
    cur_sum = sum(array[0:k])
    max_sum = cur_sum
    for i in range(k,len(array)):
        cur_sum += array[i] - array[i-k]
        max_sum = max(cur_sum,max_sum)
    return max_sum


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
result = max_sum_subarray(arr,4)
print(result)