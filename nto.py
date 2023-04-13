def count(x, y):
    return (x - 1) // y + 1


n = int(input())
m = int(input())
k = int(input())
q, r = n // m, n % m
print(count(q, k) * (m - r) + count(q + 1, k) * r)
