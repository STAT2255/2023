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

boxes = [['g', 'g'], ['s', 's'], ['g', 's']]
box = random.choice(boxes)
coin = random.choice(box)
coin

n_gold_coin = 0
n_both_gold = 0
