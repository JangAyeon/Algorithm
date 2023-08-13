def create_term2month(terms):
    _terms = {}
    for term in terms:
        t,m=term.split()
        #print(t,m)
        _terms[t] = int(m)
    return _terms
    
def date2num(date):
    #print(date)
    yyyy, mm, dd = date
    return yyyy*(28*12)+mm*28+dd
    
def isKeep(expire_num, today):
    if expire_num>today:# 보관 가능
        return True
    else: # 보관 불가능
        return False


def solution(today, terms, privacies):
    answer = []
    term2month = create_term2month(terms)
    today_date = list(map(int,today.split(".")))
    today_num = date2num(today_date)
    
    for idx, privacy in enumerate(privacies,1):
        date, term = privacy.split(" ")
        yyyy, mm, dd = list(map(int, date.split(".")))
        month = term2month[term]
        expire_num = date2num([yyyy,mm+month,dd])
        if not(isKeep(expire_num, today_num)): 
            answer.append(idx)
            
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