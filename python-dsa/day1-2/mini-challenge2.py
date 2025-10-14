#Covered: Immutability, Unpacking
nums = (10,20,30,40,50)
a,b, *rest = nums
print(f'a:{a}')
print(f'b:{b}')
print(f'rest:{rest}')