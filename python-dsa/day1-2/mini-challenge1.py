numbers = list(x for x in range(1,21))
odd = [numbers.remove(i) for i in numbers if i%2 !=0 ]
numbers.append(100)
numbers.sort(reverse=True)
numbers.pop()
print(numbers)