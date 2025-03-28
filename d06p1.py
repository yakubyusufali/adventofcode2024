class Guard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.moves = 1
        self.memory = {tuple(position)}

    def change_direction(self):
        match self.direction:
            case '<':
                self.direction = '^'
            case '^':
                self.direction = '>'
            case '>':
                self.direction = 'v'
            case 'v':
                self.direction = '<'

    def move(self):
        next_position = list(self.position)
        match self.direction:
            case '<':
                next_position[1] -= 1
            case '^':
                next_position[0] -= 1
            case '>':
                next_position[1] += 1
            case 'v':
                next_position[0] += 1
        if not 0 <= next_position[0] < len(fields) or not 0 <= next_position[1] < len(fields[0]):
            return False
        elif fields[next_position[0]][next_position[1]] == '#':
            self.change_direction()
        else:
            self.position = next_position
        return True


with open('d06_input.txt') as file:
    fields = [x for x in file.readlines()]
line = list(filter(lambda x: '^' in x, fields))[0]
position = [fields.index(line), line.index('^')]
guard = Guard(position, '^')

while guard.move():
    guard.memory.add(tuple(guard.position))

print(len(guard.memory))
