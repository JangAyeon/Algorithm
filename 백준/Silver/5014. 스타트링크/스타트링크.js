const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", (line) => {
    const [F, S, G, U, D] = line.split(" ").map(Number);
    
    function isValid(step) {
        return step >= 1 && step <= F;
    }
    
    function bfs() {
        const queue = [[S, 0]];
        const visited = Array(F + 1).fill(false);
        visited[S] = true;
        
        while (queue.length > 0) {
            const [now, process] = queue.shift();
            
            if (now === G) return process;
            
            if (isValid(now + U) && !visited[now + U]) {
                queue.push([now + U, process + 1]);
                visited[now + U] = true;
            }
            if (isValid(now - D) && !visited[now - D]) {
                queue.push([now - D, process + 1]);
                visited[now - D] = true;
            }
        }
        return "use the stairs";
    }
    
    console.log(bfs());
    rl.close();
});
