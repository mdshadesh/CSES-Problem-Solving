from collections import defaultdict

s = input()
freq = defaultdict(int)

# Count the frequency of each character
for c in s:
    freq[c] += 1

left = ""
right = ""

# Reorder the characters to form a palindrome
for c, f in freq.items():
    if f % 2 == 0:
        left += c * (f // 2)
        right = (c * (f // 2)) + right
    elif not left:
        left = c * f
    elif not right:
        right = c * f
    else:
        print("NO SOLUTION")
        exit()

# Print the palindrome
print(left + right)
