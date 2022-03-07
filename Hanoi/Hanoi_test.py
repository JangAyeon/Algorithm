from Hanoi_recur import hanoi

for i in range(1,6):
    print("### 원판이 ", i,"개인 경우")
    #원판 i개를 1반 기둥에서 3번 기둥으로 이동 (2번을 보조 기둥으로)
    total_cnt=hanoi(i, 1,3,2) 
    print("총 이동 횟수 : ",total_cnt )