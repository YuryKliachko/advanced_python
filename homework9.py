from collections import namedtuple


CAPACITY = 400
items = []

Item = namedtuple('Item', 'name weight value')
with open('items.txt', 'r') as f:
    for data in f.readlines():
        name, weight, value = data.strip().split(sep=',')
        items.append(Item(name, int(weight), int(value)))

load = 0
for item in sorted(items, key=lambda x: x.weight / x.value):
    if load + item.weight > CAPACITY:
        break
    print('{}: weight={}, value={}'.format(item.name, item.weight, item.value))
    load += item.weight
