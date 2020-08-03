# random
import random

print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 55))


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number


data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)
