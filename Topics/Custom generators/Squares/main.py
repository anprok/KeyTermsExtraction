n = int(input())


def squares(n):
    i = 1
    while i <= n:
        yield i * i
        i += 1


for n in squares(n):
    print(n)

# Don't forget to print out the first n numbers one by one here
