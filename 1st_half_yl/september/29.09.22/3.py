def reverse():
    with open('input.dat', 'rb') as f:
        data = f.read()
    with open('output.dat', 'w') as f1:
        f1.write(data[::-1])
