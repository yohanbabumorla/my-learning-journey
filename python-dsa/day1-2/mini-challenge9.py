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