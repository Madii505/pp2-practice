class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def squares(n):
    return (i * i for i in range(n))


if __name__ == "__main__":
    for num in MyRange(1, 5):
        print(num)

    print(list(even_numbers(10)))
    print(list(squares(5)))
