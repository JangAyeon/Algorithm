def solution(n):
    f = [0,1]
    if n>1: 
        for i in range(2, n+1):
            num = f[i-1]+ f[i-2]
            f.append(num)
    #print(f)
    return f[n]%1234567