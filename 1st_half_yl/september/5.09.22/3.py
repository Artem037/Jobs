alphabet = input()
n = int(input()) % len(alphabet)
print(alphabet[n:] + alphabet[:n])
print(alphabet)
print(alphabet[-n:] + alphabet[:-n])