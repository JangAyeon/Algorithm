from collections import defaultdict

def solution(genres, plays):
    answer = []
    musicDic = defaultdict(list)
    music=[]
    n = len(plays)
    for i in range(n):
        musicDic[genres[i]].append([plays[i],i])

    ## 장르별 재생수 정렬
    
    ## 장르 내 재생 수 정렬
    for k in musicDic.keys():
        musicDic[k].sort(key=lambda x:-x[0])
        total = 0
        v = musicDic[k]
        for e in v:
            total+=e[0]
        music.append([total,k])
    music.sort(key=lambda x:x[0], reverse=True)

    for _,k in music:
        m = min(len(musicDic[k]),2)
        ## print(min(len(musicDic[k]),2),k)
        for j in range(m):
            e = musicDic[k][j][1]
            answer.append(e)
            ## print("###",musicDic[k][j][1])

    return answer