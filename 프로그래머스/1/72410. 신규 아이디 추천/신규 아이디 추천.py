def solution(original_id):
    original_id= original_id.lower()
    ##print(original_id)
    new_id=[]

    for s in original_id:
        if s.isalpha() or s.isnumeric() or s in ["-","_","."]:
            if not(new_id and new_id[-1]=="." and s=="."):
                new_id.append(s)
                
        ##print(s, new_id)
    if new_id and new_id[0]==".":
        new_id.pop(0)
    if new_id and new_id[-1]==".":
        new_id.pop()
    if not new_id:
        new_id.append("a")
    if len(new_id)>15:
        new_id =new_id[:15]
        if new_id[-1]==".":
            new_id.pop()
    while len(new_id)<3:
        new_id.append(new_id[-1])
    answer = ("".join(new_id))
    return answer