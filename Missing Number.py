n = int(input())
numbers = list(map(int, input().split()))

total_sum = (n * (n + 1)) // 2

given_sum = sum(numbers)

missing_number = total_sum - given_sum

print(missing_number)
