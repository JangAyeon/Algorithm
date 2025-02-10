const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})

function isBalanced(str_) {
    const stack = []
    for (let e of str_) {
        // console.log(e, stack)
        if (e !== "[" && e !== "(" && e !== "]" && e !== ")" || e == ".") {
            continue;
        }
        if (stack.length <= 0) {
            stack.push(e);
            continue;
        }

        if (e === "[" || e === "(") {
            stack.push(e)
        } else {
            const last = stack[stack.length - 1]
            if (e == "]" && last == "[") {
                stack.pop()
            } else if (e == ")" && last == "(") {
                stack.pop()
            }
            else{
                stack.push(e)
            }


        }
        



    }
    // console.log(stack)
    return stack.length==0?"yes":"no"
}


const lines = []

rl.on("line", (line) => {
    if (line == ".") {
        rl.close()
    }
    lines.push(line.trim())

}).on("close", () => {
    // console.log("close", lines)
    for (let e of lines) {
         console.log(isBalanced(e))
    }
})

/**

[(])
())]
[ ( [ ) ]
](
( [ ( ) [ ] ] )
.
ans: 
no
no
no
no
yes
**/

/**
[(()][[])].
.

ans:
no
**/

/**
[ )].
.
ans:
no
**/

/**
([[)())]]).
ans:
no
**/