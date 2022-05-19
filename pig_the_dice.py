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

def stop(score, i):  
    player[i] += score
    print(f'your turn is over. score {score} saved.')
    
def winner_check(i):
    if player[i] >= 30:
        winner = str(i)
        return winner
    else:
        return 0
    
def calc_score(score, n):
        score += n
        print(f'total score in this turn: {score}')
        return score    

while(True):
    
    if winner in player:
        print(player)
        print(f'winnder is {winner}!')
        break
    
    for i in player.keys():
        score = 0
        
        if winner in player:
            break

        while(True):
            print(f'{i} players turn.')
            if i == 'com':
                for _ in range(rand.randrange(0,5)):
                    n = roll()
                    if n==1:
                        print('you got number 1, so your score return to 0 and turn over')
                        player['com'] = 0
                        score = 0
                        break
                    else:
                        score = calc_score(score, n)
                stop(score, 'com')
                winner = winner_check(i)
                break
            
            roll_or_stop = input('roll or stop >> ')
            if roll_or_stop == 'roll':
                n = roll()
                if n==1:
                    print('you got number 1, so your score return to 0 and turn over')
                    score = 0
                    player[i] = 0
                    break
                else: 
                    score = calc_score(score, n)

            else:
                stop(score, i)
                winner = winner_check(i)
                break

    print('--now score--')
    print(player)

