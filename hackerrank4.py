def minion_game(string):
    player1=0
    player2=0
    lent=len(string)
    for i in range(lent):
        if s[i] in "AEIOU":
            player1+=lent-i
        else:
            player2+=lent-i
    if player1>player2:
        print("Kevin",player1)
    elif player2>player1:
        print("Stuart",player2)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)