def test(i, j, pattern):
    def check(i, j, pattern):
        if pattern:
            if data[i+x][j+y] == pattern[-1] and i+x >= 0 and j+y >= 0:
                return check(i+x, j+y, pattern[:len(pattern) - 1])
            else:
                return False
        else:
            return True

    result = 0
    MOVES = (-1, 0, 1)
    for x in MOVES:
        for y in MOVES:
            try:
                if data[i+x][j+y] == pattern[-1] and i+x >= 0 and j+y >= 0 and not x == 0 == y:
                    result += check(i+x, j+y, pattern[:len(pattern)-1])
            except IndexError:
                continue
    return result


result = 0
pattern = 'XMAS'[::-1]
with open('d04_input.txt') as file:
    data = file.readlines()
for i, line in enumerate(data):
    for j, sign in enumerate(line.strip()):
        if sign == pattern[-1]:
            result += test(i, j, pattern[:len(pattern)-1])
print(result)

