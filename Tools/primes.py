# Tools for prime numbers

def is_prime(number):
    flag = True
    for j in range(2, number):
        if number % j == 0:
            flag = False

    if flag:
        return True
    return False


def primes_until(number):

    list = []
    primes = []

    for i in range(2, number):
        list.append(i)

    for i in list:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False

        if flag:
            primes.append(i)

        print(str(i*100/number) + "%")

    return primes


def prime_factors(number):
    pass


if __name__ == '__main__':
    primes_until(20)
