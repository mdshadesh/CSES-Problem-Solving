def divide_numbers(n):
    total_sum = n * (n + 1) // 2

    # Check if the sum is even
    if total_sum % 2 != 0:
        print("NO")
        return

    # Create the first set
    first_set = []
    first_set_sum = 0
    for i in range(n, 0, -1):
        if first_set_sum + i <= total_sum // 2:
            first_set.append(i)
            first_set_sum += i

    # Create the second set
    second_set = [num for num in range(1, n + 1) if num not in first_set]

    # Print the result
    print("YES")
    print(len(first_set))
    print(" ".join(map(str, first_set)))
    print(len(second_set))
    print(" ".join(map(str, second_set)))

# Read the input
n = int(input())

# Call the function
divide_numbers(n)
