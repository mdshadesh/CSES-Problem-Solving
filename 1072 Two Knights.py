n = int(input())

for k in range(1, n + 1):
    total_positions = k * k
    if k == 1:
        ways = 0
    elif k == 2:
        ways = 6
    else:
        ways = (total_positions * (total_positions - 1)) // 2 - 4 * (k - 1) * (k - 2)

    print(ways)
