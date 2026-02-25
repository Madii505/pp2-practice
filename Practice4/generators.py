# Squares up to N
def squares_n(n):
    for i in range(n + 1):
        yield i * i

# Even numbers 0 to n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Countdown from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Example usage
if __name__ == "__main__":
    print(list(squares_n(5)))
    print(",".join(map(str, even_numbers(10))))
    print(list(divisible_by_3_and_4(50)))
    for s in squares(3, 6):
        print(s)
    print(list(countdown(5)))