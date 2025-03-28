def test(i, j):
    try:
        if data[i-1][j-1] == pattern[data[i+1][j+1]] and data[i+1][j-1] == pattern[data[i-1][j+1]]:
            return True
        return False
    except KeyError:
        return False


result = 0
pattern = {'M': 'S', 'S': 'M'}
with open('d04_input.txt') as file:
    data = file.readlines()
for i, line in enumerate(data[1:-1], start=1):
    for j, sign in enumerate(line.strip()[1:-1], start=1):
        if sign == 'A':
            result += test(i, j)
print(result)
