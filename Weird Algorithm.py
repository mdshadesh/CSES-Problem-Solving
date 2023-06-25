n = int(input())
sequence = [str(n)]

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    sequence.append(str(n))

output = ' '.join(sequence)
print(output)
