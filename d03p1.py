import re


def prepare_and_clean_data(data):
    temp_data = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    return [tuple(map(lambda x: int(x), record.lstrip('mul(').rstrip(')').split(','))) for record in temp_data]


def result(data):
    prepared_data = ''.join(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data))
    cleaned_data = prepare_and_clean_data(prepared_data)
    return sum(x * y for x, y in cleaned_data)


with open('d03_input.txt') as file:
    data = file.read()
print(result(data))
