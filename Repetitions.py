sequence = input()

current_char = ''
current_count = 0
longest_length = 0

for char in sequence:
    if char == current_char:
        current_count += 1
    else:
        current_char = char
        current_count = 1

    longest_length = max(longest_length, current_count)

print(longest_length)
