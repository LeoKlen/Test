# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
def rps(p1, p2):
    #your code here
    if (p1 == "scissors" and p2 == "paper" or p1 == "paper" and p2 == "rock" or p1 == "rock" and p2 == "scissors"):
        ans = "Player 1 won!"
    elif (p2 == "scissors" and p1 == "paper" or p2 == "paper" and p1 == "rock" or p2 == "rock" and p1 == "scissors"):
        ans = "Player 2 won!"
    else:
        ans = "Draw!"
    return ans