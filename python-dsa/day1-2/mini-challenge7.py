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