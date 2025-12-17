
var WordDictionary = function() {
     this.root={
        child:{},
        isEnd:false
     }
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let node = this.root
    for(const ch of word){
        if(!node.child[ch]){
            node.child[ch]={
                child:{},
                isEnd:false
            }
        }
        node=node.child[ch]
    }
    node.isEnd = true
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    

    const dfs=(idx, node)=>{
        if(idx == word.length){
            return node.isEnd
        }
        const ch = word[idx]

        if(ch=="."){
            for(let k of [...Object.keys(node.child)]){
                if(dfs(idx+1, node.child[k])){return true}
            }
            return false
        }

        if(!node.child[ch]){return false}
        return dfs(idx+1, node.child[ch])
    }

    return dfs(0, this.root)
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */