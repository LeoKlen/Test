def is_prime(a):
    i = 2
    while i < a:
        if a % i == 0:
            return False
        else:
            i += 1

    return True
