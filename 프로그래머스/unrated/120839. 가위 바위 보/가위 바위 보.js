function solution(rsp){
	let answer = {"0":"5","2":"0","5":"2"};
	return [...rsp].map(v=>answer[v]).join("")
}