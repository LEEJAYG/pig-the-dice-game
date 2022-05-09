# pig the dice

import random as rand

num = int(input('플레이어 수: '))
player = {str(p):0 for p in range(1, num+1)}
player['com'] = 0

for i in player.keys():
    while(True):
        print(f'{i}번째 player님의 차례입니다.')
        roll_or_stop = input('roll or stop >> ')
        if roll_or_stop == 'roll':
            n = rand.randrange(1,7)
            print(f'숫자 {n}이 나왔습니다.')
        else:
            break
