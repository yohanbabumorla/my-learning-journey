def merge_arrays(array1,array2):
    left = right = 0
    merged = []
    while left < len(array1) and right < len(array2):
        if array1[left] < array2[right]:
            merged.append(array1[left])
            left += 1
        else:
            merged.append(array2[right])
            right += 1
    merged.extend(array1[left:])
    merged.extend(array2[right:])
    return merged


print(merge_arrays([1,5,8], [2,4,7]))
