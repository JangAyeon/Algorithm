def solution(arr1, arr2):
    answer = []
    for row in arr1:
        t =[]
        for dx in range(len(arr2[0])):
            temp = 0
            for dy in range(len(row)):
                temp+=row[dy]*arr2[dy][dx]
            t.append(temp)
        answer.append(t)
    return answer