def get_distance(curr,target):

    move = abs(curr-target)//3+abs(curr-target)%3
    ##print(curr, target, move+1)
    return move
        


def solution(numbers, hand):
    answer = ''
    l_loc, r_loc=10,12
    for idx in range(len(numbers)):
        if numbers[idx]==0:
            numbers[idx]=11
            
    for number in numbers:
        ##print(number, l_loc, r_loc)
        if number in [1,4,7]:
            answer+=("L")
            l_loc=number
        elif number in [3,6,9]:
            answer+=("R")
            r_loc=number
        else:
            
            r,l =  get_distance(r_loc,number),get_distance(l_loc,number)
            ##print(number,"(l,r)", l,r)
            if r>l:
                l_loc = number
                answer+=("L")
            elif r<l:
                r_loc=number
                answer+=("R")
                
            else: ## 거리 같은 경우
                if hand == "right":
                    r_loc =number
                    answer+=("R")
                else:
                    l_loc=number
                    answer+=("L")
   
    return answer