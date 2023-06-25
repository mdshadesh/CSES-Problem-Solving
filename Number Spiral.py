t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    n = max(x,y)
    print(n*(n-1)+1+(-1)**n*(x-y))
