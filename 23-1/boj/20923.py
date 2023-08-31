import sys
from collections import deque
input = sys.stdin.readline

# Input
card_cnt, turn_limit = map(int, input().split())
do_card = deque()
su_card = deque()
for _ in range(card_cnt):
    d, s = map(int, input().split())
    do_card.append(d)
    su_card.append(s)

#
do_ground = deque()
su_ground = deque()


def bell():
    
    ## 수연이가 이기는 경우
    if do_ground and su_ground and do_ground[-1] + su_ground[-1] == 5:
        su_card.extendleft(do_ground)
        su_card.extendleft(su_ground)
        su_ground.clear()
        do_ground.clear()
        return
    
    ## 도도가 이기는 경우
    if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
        do_card.extendleft(su_ground)
        do_card.extendleft(do_ground)
        su_ground.clear()
        do_ground.clear()
        return


def game():
    turn = 0
    check = True
    while True:
        if check:
            do_ground.append(do_card.pop())
            check = False
            ## 도도의 덱이 비어있는 경우 패배
            if not do_card:
                return "su"
        else:
            su_ground.append(su_card.pop())
            check = True
            ## 수연이의 덱이 비어있는 경우 패배
            if not su_card:
                return "do"
        bell()
        turn += 1
        if turn == turn_limit:
            break


    if len(su_card) > len(do_card):
        return 'su'
    elif len(su_card) < len(do_card):
        return 'do'
    else:
        return 'dosu'


print(game())
