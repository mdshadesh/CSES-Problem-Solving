t = int(input())

while t > 0:
    a,b = [int(x) for x in input().split()]
    if (a*2 <b) or (b*2 <a) or ((a+b)%3 != 0):
        print("NO")
    else:
        print("YES")
    t -= 1