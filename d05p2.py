def test_and_repair(rules, updates):
    rules = [x.split('|') for x in rules.split()]
    updates = [x.split(',') for x in updates.split()]
    result = 0
    for update in updates:
        correct = True
        for num in update[1:-1]:
            prev_args = update[:update.index(num)]
            post_args = update[update.index(num) + 1:]
            prev_mistakes = [x for x in prev_args if x in [y[1] for y in filter(lambda rule: rule[0] == num, rules)]]
            post_mistakes = [x for x in post_args if x in [y[0] for y in filter(lambda rule: rule[1] == num, rules)]]
            if prev_mistakes:
                update.insert(int(update.index(prev_mistakes[0])), update.pop(update.index(num)))
                correct = False
            elif post_mistakes:
                update.insert(int(update.index(post_mistakes[-1])), update.pop(update.index(num)))
                correct = False
        if not correct:
            result += int(update[len(update) // 2])
    return result

with open('d05_input.txt') as file:
    rules, updates = file.read().split('\n\n')
result = test_and_repair(rules, updates)


print(result)
