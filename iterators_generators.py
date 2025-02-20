#1 Generator for Squares of Numbers Up to N
def squares_up_to_n(n):
    for i in range(n + 1):
        yield i ** 2

for i in squares_up_to_n(5):
    print(i)

#2 Generator for Even Numbers Between 0 and N (Comma Separated)
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Enter a number: "))
print(",".join(map(str, even_numbers(n))))

#3 Generator for Numbers Divisible by 3 and 4 in a Given Range
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num)

#4 Generator for Squares of Numbers from (a) to (b)
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = 2, 6  
for sq in squares(a, b):
    print(sq)

#5. Generator for Numbers from N Down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))
for num in countdown(n):
    print(num)