# pig the dice

import random as rand

num = int(input('플레이어 수: '))
player = {str(p):0 for p in range(1, num+1)}
player['com'] = 0
print(player)
