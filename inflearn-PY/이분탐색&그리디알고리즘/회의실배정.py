#code from lecture

n=int(input()) #회의 갯수
meeting = [] #회의 스케줄
for i in range(n):
    start,end=map(int,input().split())
    meeting.append((start,end)) 
    #시작 시간, 끝나는 시간 튜플 형태로 추가

meeting.sort(key=lambda x : (x[1],x[0]))
#원래 sort는 앞의 값(start)기준으로 정렬됨
#key값 파라미터를 조정해 뒤의 값(end)기준으로 정렬

curr_end=0
cnt=0
for start,end in meeting:
    if start>=curr_end:
        curr_end=end
        cnt+=1

print(cnt)
