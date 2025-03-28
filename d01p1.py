list1, list2 = [], []
result = 0
with open('d01_input.txt') as file:
    data = [x.rstrip('\n') for x in file.readlines()]
for pair in data:
    x, y = pair.split('   ')
    list1.append(x)
    list2.append(y)
list1.sort(reverse=True)
list2.sort(reverse=True)
while list1:
    x = int(list1.pop(-1))
    y = int(list2.pop(-1))
    result += abs(x - y)
print(result)
