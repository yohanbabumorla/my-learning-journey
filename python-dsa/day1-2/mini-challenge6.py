even = [x**2 for x in range(0,11) if x%2 == 0]
generator_expression = (x for x in even)
while True:
    try:
        print(next(generator_expression))
    except StopIteration:
        break
