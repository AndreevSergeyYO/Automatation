n = int(input())


def fizz_bazz(n):
    for n in range(1, n+1):
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBazz")
        elif n % 5 == 0:
            print("Bazz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)


fizz_bazz(n)
