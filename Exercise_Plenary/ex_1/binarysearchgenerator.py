import random as rnd

N = 100
K = 10

start = -N
stop = N


def gennums(start, stop, step):
    x = start + rnd.randint(0, step)
    xs = []

    while x < stop:
        xs.append(x)
        x += rnd.randint(0, step)
    return xs


def oracle(arr, queries):
    s = set(arr)
    answers = []
    for q in queries:
        answers.append(q in s)
    return answers


arr = gennums(-N, N, K)
queries = gennums(-N, N, K)

print(len(arr))
print("\n".join(map(str, arr)))

print(len(queries))
print("\n".join(map(str, queries)))

print(len(queries))
print("\n".join(map(str, oracle(arr, queries))))
