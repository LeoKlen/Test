def can_eat(a, b):
    if abs(a[0] - b[0]) == 2 and abs(a[1] - b[1]) == 1:
        return True
    if abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 2:
        return True
    else:
        return False
