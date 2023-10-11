
import math


def trouver_disposition(N):
    j = 1
    i = 1
    disposition = []
    for i in range(N):
        for j in range(N):
            if math.gcd(i, j) == 1 and i+j == N and i > 0 and j > 0:
                disposition.append((i, j))
    return disposition


print(trouver_disposition(4))
