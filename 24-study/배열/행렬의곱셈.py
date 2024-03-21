def solution(arr1, arr2):
    answer = []
    for row in arr1:
        r =[]
        for dx in range(len(arr2[0])):
            temp = 0
            for dy in range(len(row)):
                temp+=row[dy]*arr2[dy][dx]
            r.append(temp)
        answer.append(r)
    return answer