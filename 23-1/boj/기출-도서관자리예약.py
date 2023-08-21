import sys
input = sys.stdin.readline
n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
rooms = []


for i in range(n):
	rooms.append([start[i], end[i]])
rooms.sort(key = lambda x :(x[1]))

end_1, end_2 = -1, -1
answer =1
#print(rooms)


for s, e in rooms[1:]:
	if end_1<=s:
		end_1=e
		answer+=1
	elif end_2<=s:
		end_2 = end_1
		end_1=e
		answer+=1
		
print(answer)