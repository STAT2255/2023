import random
random.seed(1)
up = 0
n = 10
for i in range(n):
    up += random.uniform(1, 15) < 13
    # up = up + (random.uniform(1, 15) < 13)
up / n

n = 1000
results = [random.uniform(1, 15) < 13 for i in range(n)]
sum(results) / n

A = [2, 2, 4, 4, 9, 9]
B = [1, 1, 6, 6, 8, 8]
C = [3, 3, 5, 5, 7, 7]

n = 10000

ab = 0
for i in range(n):
    ab += random.choice(A) < random.choice(B)
ab / n

bc = 0
for i in range(n):
    bc += random.choice(B) < random.choice(C)
bc / n

ca = 0
for i in range(n):
    ca += random.choice(C) < random.choice(A)
ca / n

def play(a, b, n = 1000):
    ab = 0
    for i in range(n):
        ab += random.choice(a) < random.choice(b)
    return ab / n

play(A, B)
play(B, C)
play(A, C)

# Version 1
n_gold_coin = 0
n_both_gold = 0
N = 1000
for i in range(N):
    boxes = [['g', 'g'], ['s', 's'], ['g', 's']]
    box = random.choice(boxes)
    coin = random.choice(box)
    if coin == 'g':
        n_gold_coin = n_gold_coin + 1
        if box == ['g', 'g']:
            n_both_gold += 1
n_both_gold / n_gold_coin 

# version 2
def bert():
    boxes = [['g', 'g'], ['s', 's'], ['g', 's']]
    box = random.choice(boxes)
    coin = random.choice(box)
    return box, coin

n_gold_coin = 0
n_both_gold = 0
N = 1000
random.seed(1)
for i in range(N):
    box, coin = bert()
    if coin == 'g':
        n_gold_coin = n_gold_coin + 1
        if box == ['g', 'g']:
            n_both_gold += 1
n_both_gold / n_gold_coin 

bert()

def birth(n_room, n_year):
    year = list(range(1, n_year+1))
    room = []
    for i in range(n_room):
        room.append(random.choice(year))
        common_birthday = len(room) == len(set(room))
    return common_birthday

N = 1000
n = 0
for i in range(N):
    n += birth(500, 2400000)
n / N

random.choices([1, 2, 3], k=4)

def mont():
    car = random.choice([1, 2, 3])
    choice = 1
    if car == 1:
        host = random.choice([2, 3])
    if car == 2:
        host = 3
    if car == 3:
        host = 2
    return host, car 
mont()
