# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    ans = 0
    for i in range(0, len(numbers)):
        slog = pow(numbers[i],2)
        ans = ans+slog
    return ans