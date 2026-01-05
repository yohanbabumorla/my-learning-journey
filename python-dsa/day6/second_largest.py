def second_largest_element(array):
    first_max = float("-inf")
    sec_max = float("-inf")
    for i in array:
        if i > first_max:
            sec_max = first_max
            first_max = i
        elif i > sec_max and i != first_max:
            sec_max = i

    return sec_max


arr = [1,4,2,3,7,8,4,5,43,745,23,345,567,23,42]
result = second_largest_element(arr)
print(f"\nThe second largest element in tha array {arr} is {result}")
    # time complexity is O(n) and space complexity is O(2) => O(1)