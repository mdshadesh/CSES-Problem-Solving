n = int(input())
array = list(map(int, input().split()))

moves = 0
prev = array[0]

for i in range(1, n):
    if array[i] < prev:
        moves += prev - array[i]
    else:
        prev = array[i]

print(moves)
