def getPersonalDateTerm(info):
    date,term = info.split(" ")
    year,month,day = list(map(int, date.split(".")))
    return year, month, day,term

def createTermPeriod(terms):
    _terms = {}
    for term in terms:
        t, m = term.split()
        _terms[t] = int(m)
    return _terms

def createLastDate(period, yyyy,mm,dd):
    m = mm + period
    y = yyyy 
    d = dd
    if m>12:

        if m%12==0: # 24월, 36월, 48월....
            y = y + (m//12)-1
            m = m%12
        else:
            y+=m//12
            m=m%12
        if m==0: # 추가된 달이 모두 년수로 똑나눠 떨어진 경우
            m=12
    if d==0:
        d = 28
        m-=1
        if m==0:
            m=12
            
    #print(y,m,d)
    return  y, m,d

def checkDate(yyyy,mm,dd, today):
    y,m,d = list(map(int, today.split("."))) # 오늘
    
    # 보관이 불가능한 경우
    if yyyy<y:
        return False
    if (yyyy==y and mm<m):
        return False
    if (yyyy==y and mm==m and dd<=d):
        return False
    return True
    

def solution(today, terms, privacies):
    answer = []
    termPeriod = createTermPeriod(terms)
    #print(termPeriod)
    for idx, info in enumerate(privacies):
        yyyy, mm, dd, t = getPersonalDateTerm(info)
        _yyyy,_mm,_dd = createLastDate(termPeriod[t], yyyy,mm,dd)
        #print("last date", _yyyy,_mm,_dd)
        if not(checkDate(_yyyy,_mm,_dd, today)):
            answer.append(idx+1)


    return answer




input1 = [
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
]
input2 = [
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
]

# [1]
input3=[
    "2016.02.15", ["A 100"], ["2000.06.16 A", "2008.02.15 A"]]

# [2]
input4 = [
    "2019.12.09", ["A 12"], ["2018.12.10 A", "2010.10.10 A"]
    
    ]
    
# [1,2]
input5 = ["2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]]

inputs = [input1,input2, input3, input4, input5]
for today, terms, privacies in inputs:
    print(solution(today, terms, privacies))