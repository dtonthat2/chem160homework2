from random import choices
nrolls = 15000
player1wins = 0
for i in range(nrolls):
    dice2 = choices(range(1,7),k = 2)
    if dice2[0] == dice2[1]:
        continue
    dice1 = choices(range(1,7),k = 3)
    dice1.sort(reverse=True)
    if dice1.count(2) >1:
        continue
    if dice1[0]+dice1[1] > dice2[0]+dice2[1]:
        player1wins =  player1wins+1
print("Ratio of player1 wins =",player1wins/nrolls)