var numberOfSubstrings = function(s) {
    const count = [0, 0, 0]; // a,b,c count
    const N = s.length;
    let start = 0;
    let result = 0;

    for (let end = 0; end < N; end++) {
        count[s[end].charCodeAt(0) - 97]++;

        // abc 모두 포함될 때 start를 가능한 만큼 밀기
        while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
            result += (N - end);  
            count[s[start].charCodeAt(0) - 97]--;
            start++;
        }
    }
    return result;
};
