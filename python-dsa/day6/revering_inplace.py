#reverse an array in-place(without using any temp or any kind of new variables )
def reverse_array(array):
    for i in range(int(len(array)/2)):
        array[i], array[-1*(i+1)] = array[-1*(i+1)], array[i]
        #array[i] , array[~i] = array[~i], array[i] same as above using bitwise not operator
    return array

arr = [1,2,3,4,5,6]
print(reverse_array(arr))