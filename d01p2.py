list1, list2 = [], []
result = 0
with open('d01_input.txt') as file:
    data = [x.rstrip('\n') for x in file.readlines()]
for pair in data:
    x, y = pair.split('   ')
    list1.append(x)
    list2.append(y)
for number in list1:
    x = int(number) * list2.count(number)
    result += x
print(result)
