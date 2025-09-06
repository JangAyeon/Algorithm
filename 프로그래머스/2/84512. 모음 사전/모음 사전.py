def solution(word):
    answer = 0
    N = len(word)
    arr = []
    dictionary = [ 'A', 'E', 'I', 'O', 'U']
    def dfs(lst):
        if(len(dictionary)==len(lst)):
            return
        for i in range(len(dictionary)):
            w = lst + [dictionary[i]]
            arr.append("".join(w))
            dfs(w)
    dfs([])
    ## print(arr)
    print(arr.index(word))
    return arr.index(word)+1