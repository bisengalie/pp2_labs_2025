import time
import math
from functools import reduce

# 1. Multiply all numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# 2. Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Calculate the square root after a delay in milliseconds
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

# 5. Check if all elements in a tuple are True
def all_true(t):
    return all(t)

# --- Examples of usage ---
# 1. Multiply numbers in a list
numbers = [2, 3, 4, 5]
print(f"Product of the list {numbers}: {multiply_list(numbers)}")

# 2. Count uppercase and lowercase letters in a string
text = "Hello World"
upper_count, lower_count = count_case(text)
print(f"In the string '{text}', uppercase letters: {upper_count}, lowercase letters: {lower_count}")

# 3. Check if a string is a palindrome
palindrome_text = "madam"
print(f"Is '{palindrome_text}' a palindrome? {is_palindrome(palindrome_text)}")

# 4. Square root after a delay
number = 25100
delay = 2123
result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} ms: {result}")

# 5. Check if all elements in a tuple are True
values = (True, True, False)
print(f"Are all elements in {values} true? {all_true(values)}")

values = (1, 2, 3)
print(f"Are all elements in {values} true? {all_true(values)}")