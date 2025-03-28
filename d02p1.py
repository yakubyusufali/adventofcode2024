def check_report(report):
    if all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)):
        print('mal', report)
        return True
    elif all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)):
        print('ros', report)
        return True
    return False


result = 0
with open('d02_input.txt') as file:
    data = [[int(num) for num in x.rstrip('\n').split(' ')] for x in file.readlines()]
for h, report in enumerate(data):
    print(h)
    if check_report(report):
        result += 1
print(result)
