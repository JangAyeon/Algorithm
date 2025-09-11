function solution(people, limit) {
    people.sort((a, b) => a - b); // 오름차순 정렬
    let i = 0;                    // 가장 가벼운 사람 index
    let j = people.length - 1;    // 가장 무거운 사람 index
    let boats = 0;

    while (i <= j) {
        if (people[i] + people[j] <= limit) {
            i++; // 가벼운 사람 태움
        }
        j--; // 무거운 사람은 항상 태움
        boats++;
    }

    return boats;
}
