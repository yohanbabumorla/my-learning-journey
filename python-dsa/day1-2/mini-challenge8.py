try:
    num1, num2 = map(int, input(">").split())
    val = num1/num2
    print(val)
except ZeroDivisionError:
    print("sorry zero can not divide!")
except ValueError:
    print("only enter two numbers separated by space")
finally:
    print("Operation complete")
