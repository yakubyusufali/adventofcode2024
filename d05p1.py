with open('d05_input.txt') as file:
    rules, updates = file.read().split('\n\n')
rules = [x.split('|') for x in rules.split()]
updates = [x.split(',') for x in updates.split()]
result = 0
for update in updates:
    correct = True
    for num in update[1:-1]:
        prev_args = update[:update.index(num)]
        post_args = update[update.index(num) + 1:]
        if (any(True for x in prev_args if x in [y[1] for y in filter(lambda rule: rule[0] == num, rules)]) or
                any(True for x in post_args if x in [y[0] for y in filter(lambda rule: rule[1] == num, rules)])):
            break
    else:
        mid_arg = update[len(update) // 2]
        result += int(mid_arg)
print(result)
