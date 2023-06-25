n = int(input())

# Check if a beautiful permutation is possible
if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    # Print even numbers first
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    
    # Print odd numbers
    for i in range(1, n + 1, 2):
        print(i, end=" ")
