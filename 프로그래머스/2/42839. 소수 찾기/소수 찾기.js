function solution(numbers) {
    const n = numbers.length;
    const arr = numbers.split("").map(Number); // 문자열 → 숫자 배열
    let visited = Array.from({ length: n }).fill(false);
    const nums = new Set();

    function dfs(targetLength, lst) {
        if (lst.length === targetLength) {
            nums.add(Number(lst.join("")));
            return;
        }
        for (let i = 0; i < n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            dfs(targetLength, [...lst, arr[i]]);
            visited[i] = false;
        }
    }

    for (let i = 1; i <= n; i++) {
        dfs(i, []);
    }

    function isPrime(num) {
        if (num < 2) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    }

    let count = 0;
    for (let e of nums) {
        if (isPrime(e)) count++;
    }

    return count;
}
