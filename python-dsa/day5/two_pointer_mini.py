#Write a Python function that checks if a sorted array contains any pair of numbers whose sum equals a given target.If found, return True; else False.
def paired_sum(array,target):
    left, right = 0, len(array)-1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False


arr = [1, 2, 4, 7, 11, 15]
result = paired_sum(arr,15)
print(result)