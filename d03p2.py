import re


def find_data(data):
    first_part = data[:data.index('don\'t()')]
    middle_part = ''.join(re.findall(r'(?s)do\(\)(.*?)don\'t\(\)', data))
    last_part = data[data.rindex('do()'):]
    return first_part + middle_part + last_part


def prepare_and_clean_data(data):
    temp_data = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    return [tuple(map(lambda x: int(x), record.lstrip('mul(').rstrip(')').split(','))) for record in temp_data]


def result(data):
    working_parts = find_data(data)
    cleaned_data = prepare_and_clean_data(working_parts)
    return sum(x * y for x, y in cleaned_data)


with open('d03_input.txt') as file:
    data = file.read()
print(result(data))
