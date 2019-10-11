import random
import string

print(random.randint(1, 10))

print(random.choice([2, 4, 8]))

print(random.choices([6, 9, 10], k=2))
print(string.ascii_letters)
print(string.digits)

print("".join(random.choices(string.digits + string.ascii_letters, k=8)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)

print(numbers)
