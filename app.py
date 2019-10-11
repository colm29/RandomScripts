from collections import deque
from array import array

prices = [('chicken', 1), ('ham', 6), ('zebra', 2)]


prices = list(map(lambda item: item[1], prices))
print(prices)

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

newlist = [i for i in queue if i < 0]
print(newlist)

test_tuple = 1, 'a', 7
print(test_tuple)
print(type(test_tuple))

x = 10
y = 11

x, y = y, x
print(x, y)

arr = array('i', range(0, 19))
print(arr)
list_range = list(range(0, 2))
print(list_range)

print(type(range(0, 19)))

the_list = [3, 8, 8, 7, 4, 7, 4]
set1 = set(the_list)
set2 = {10, 4, 1, 22}
print(set1 | set2)
print(set1 & set2)
print(set1-set2)
print(set1 ^ set2)

dct = dict(x=1, y=2)
if 'x' in dct:
    print(dct['x'])

print(dct.get('x', 'hello'))
print(dct.get('q', 'hello'))

print(list(range(3)))


def find_most_repeated(input):
    dct = {}

    for i in input:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

    return sorted(dct.items(), key=lambda x: x[1], reverse=True)[0][0]


print(find_most_repeated('this is a common interview question'))


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input


print(fizz_buzz(7))


def print_even():
    counter = 0
    for n in range(1, 10):
        if n % 2 == 0:
            print(n)
            counter += 1
    print(f'There are {counter} numbers')


print_even()
