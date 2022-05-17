# pig the dice

import random as rand

num = int(input('player num: '))
player = {str(p):0 for p in range(1, num+1)}
player['com'] = 0
winner = ''

def roll():
    n = rand.randrange(1,7)
    print(f'your number is {n}')
    return n

def stop(i, score):
    player[i] += score   
    print(f'your turn is over. score {score} saved.')
    
def winner(i):
    if player[i] >= 50:
        winner = i
    return winner
    
def com_play():
    for roll in range(rand.randrange(0,10)):
        n = roll()
        if n==1:
            player[i] = 0
            break
        else:
            score += n
            player[i] += score
            winner = winner()
    print(f'your turn is over. score {score} saved.')


while(True):

    for i in player.keys():
        score = 0

        while(True):
            print(f'{i} players turn.')
            if i == 'com':
                for roll in range(rand.randrange(0,10)):
                    n = rand.randrange(1,7)
                    if n==1:
                        player[i] = 0
                        break
                    else:
                        score += n
                        player[i] += score
                        if player[i] >= 150:
                            winner = i
                            break
                print(f'yout turn is over. score {score} saved.')
                break


            roll_or_stop = input('roll or stop >> ')
            if roll_or_stop == 'roll':
                n = rand.randrange(1,7)
                print(f'your number is {n}')
                if n==1:
                    print('you got number 1, so your score return to 0 and turn over')
                    player[i] = 0
                    break
                else: 
                    score += n
                    print(f'total score in this turn: {score}')
                    player[i] += score
                    if player[i] >= 150:
                        winner = i
                        break
            else:
                player[i] += score
                print(f'your turn is over. score {score} saved.')
                break

    if winner in player:
        print(player)
        print(f'winnder is {winner}!')
        break

    print('--now score--')
    print(player)
