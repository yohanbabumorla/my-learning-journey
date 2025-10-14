# 📘 Python DSA — Day 1 & 2

> *“Start simple, stay consistent, and keep improving.”*  

### 🧾 Topics & Mini Challenges Recap

#### 🟦 Lists
✅ Covered: Indexing, Slicing, Append, Pop, Sort, Comprehension  
🎯 **Mini Challenge:**
```python
# Create list 1–20, remove odd numbers, append 100, sort descending, pop last item
numbers = [i for i in range(1, 21)]
numbers = [n for n in numbers if n % 2 == 0]
numbers.append(100)
numbers.sort(reverse=True)
numbers.pop()
print(numbers)

🟩 Tuples
✅ Covered: Immutability, Unpacking
🎯 Mini Challenge:
#Covered: Immutability, Unpacking
nums = (10,20,30,40,50)
a,b, *rest = nums
print(f'a:{a}')
print(f'b:{b}')
print(f'rest:{rest}')

🟨 Sets

✅ Covered: Union, Intersection, Difference
🎯 Mini Challenge:
#sets
A = {1,2,3,4}
B = {3,4,5,6}
print('Union:',A.union(B))
print('Intersection:',A.intersection(B))
print('A-B:',A-B)
print('B-A:',B-A)

🟧 Dictionaries

✅ Covered: Key-Value Access, Methods
🎯 Mini Challenge:
#dictionaries
student_data = {
    "student1": 89,
    "student2": 76,
    "student3": 74,
    "student4": 98,
    "student5": 87
}
student_data['student1'] = 100 #updating
student_data['student6']= 45 #adding
student_data.pop('student5') #removing
print(student_data)
🟥 Strings

✅ Covered: Slicing, Methods, Formatting
🎯 Mini Challenge:
text = "Python is Powerful"
sliced_part = text[10:]
sliced_part.upper()
print(f'"The Keyword is:{sliced_part}"')

🟦 List Comprehension vs Generator Expression

✅ Covered: Syntax, Use Cases, Differences
🎯 Mini Challenge:
even = [x**2 for x in range(0,11) if x%2 == 0]
generator_expression = (x for x in even)
while True:
    try:
        print(next(generator_expression))
    except StopIteration:
        break


🟩 enumerate, zip, map, filter, reduce

✅ Covered: Syntax, Use Cases, Examples
🎯 Mini Challenge: Student Score Pipeline
from functools import reduce

student_names = ['yohan','madhav','bala']
student_scores = [87, 45, 90]

#step 1 zip()
paired = list(zip(student_names,student_scores))
print(paired)

#step 2 filter()
filtered = list(filter(lambda x: x[1] <= 60,paired))
print(filtered)

#map()
mapped_data = list(map(lambda x: f"{x[0]}: {x[1]}", filtered))
print(mapped_data)

#enumerat()
enumerated = [f"{i}. {entry}" for i,entry in enumerate(mapped_data,start=1)]
print("Final list:")
for line in enumerated:
    print(list)


#redusing
report = reduce(lambda x,y: x + '\n' + y, enumerated)
print("\n Final report \n",report)

🟥 Exception Handling

✅ Covered: try, except, finally
🎯 Mini Challenge: Safe Division
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


🟦 File Handling
✅ Covered: Reading, Writing, Best Practices
🎯 Mini Challenge: Word Frequency Counter
with open('input.txt','r')as file:
    content = file.read()
content.lower()
content = content.replace(" ","").lower()
content = content.replace('\n','').lower()
m = {}
for j in content:
    if j in m:
        m[j] += 1
    else:
        m[j] = 1
print(m)
sorted_data = dict(sorted(m.items()))
print(sorted_data)
sorted_data = str(sorted_data)
#writing
with open('output.txt','w')as file:
    file.write(sorted_data)
✅ Summary

✔️ Built strong Python foundations
✔️ Completed 9 practical mini-challenges
✔️ Learned file handling, exceptions, and comprehension
✔️ Uploaded all code to GitHub

End of Day 1–2

