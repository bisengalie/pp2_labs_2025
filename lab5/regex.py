import re

# 1. Match a string that has 'a' followed by zero or more 'b's
def match_a_b_star(string):
    return bool(re.fullmatch(r'ab*', string))

# 2. Match a string that has 'a' followed by two to three 'b's
def match_a_bb_or_bbb(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

# 3. Find sequences of lowercase letters joined with an underscore
def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+(?:_[a-z]+)*\b', string)

# 4. Find sequences where an uppercase letter is followed by lowercase letters
def find_capital_followed_by_lowercase(string):
    return re.findall(r'[A-Z][a-z]+', string)

# 5. Match a string that has 'a', followed by anything, ending in 'b'
def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

# 6. Replace all occurrences of space, comma, or dot with a colon
def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

# 7. Convert a snake_case string to CamelCase
def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

# 8. Split a string at uppercase letters
def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# 9. Insert spaces before words starting with capital letters
def insert_spaces_before_capitals(string):
    return re.sub(r'([A-Z])', r' \1', string).strip()

# 10. Convert a given CamelCase string to snake_case
def camel_to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()

# Example usage
print(match_a_b_star("abbb"))  # True
print(match_a_bb_or_bbb("abb"))  # True
print(find_lowercase_with_underscore("hello_world test_example example_text"))
print(find_capital_followed_by_lowercase("Hello World Test Example"))
print(match_a_anything_b("axb"))  # True
print(replace_with_colon("Hello, world. This is a test"))
print(snake_to_camel("hello_world_test"))  # HelloWorldTest
print(split_at_uppercase("HelloWorldTest"))  # ['Hello', 'World', 'Test']
print(insert_spaces_before_capitals("HelloWorldTest"))  # "Hello World Test"
print(camel_to_snake("HelloWorldTest"))  # "hello_world_test"