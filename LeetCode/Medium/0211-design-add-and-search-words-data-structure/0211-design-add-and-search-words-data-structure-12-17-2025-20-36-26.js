var WordDictionary = function () {
  this.root = {
    children: {},
    isEnd: false,
  };
};

WordDictionary.prototype.addWord = function (word) {
  let node = this.root;

  for (const ch of word) {
    if (!node.children[ch]) {
      node.children[ch] = {
        children: {},
        isEnd: false,
      };
    }
    node = node.children[ch];
  }

  node.isEnd = true;
};

WordDictionary.prototype.search = function (word) {
  const dfs = (index, node) => {
    if (index === word.length) {
      return node.isEnd;
    }

    const ch = word[index];

    if (ch === ".") {
      for (const key in node.children) {
        if (dfs(index + 1, node.children[key])) {
          return true;
        }
      }
      return false;
    }

    if (!node.children[ch]) return false;
    return dfs(index + 1, node.children[ch]);
  };

  return dfs(0, this.root);
};
