function solution(nodeinfo) {
  // 1. 각 노드에 번호(index + 1) 부여
  const nodes = nodeinfo.map(([x, y], idx) => ({ x, y, idx: idx + 1 }));

  // 2. y 기준 내림차순, y가 같으면 x 기준 오름차순 정렬
  nodes.sort((a, b) => {
    if (a.y === b.y) return a.x - b.x;
    return b.y - a.y;
  });

  // 3. 트리 구성 함수
  class Node {
    constructor(x, y, idx) {
      this.x = x;
      this.y = y;
      this.idx = idx;
      this.left = null;
      this.right = null;
    }
  }

  const root = new Node(nodes[0].x, nodes[0].y, nodes[0].idx);

  // 삽입 함수
  const insert = (parent, child) => {
    if (child.x < parent.x) {
      if (parent.left === null) parent.left = child;
      else insert(parent.left, child);
    } else {
      if (parent.right === null) parent.right = child;
      else insert(parent.right, child);
    }
  };

  // 4. 트리 구성
  for (let i = 1; i < nodes.length; i++) {
    const child = new Node(nodes[i].x, nodes[i].y, nodes[i].idx);
    insert(root, child);
  }

  // 5. 순회 결과 저장
  const preorder = [];
  const postorder = [];

  const preorderTraverse = (node) => {
    if (!node) return;
    preorder.push(node.idx);
    preorderTraverse(node.left);
    preorderTraverse(node.right);
  };

  const postorderTraverse = (node) => {
    if (!node) return;
    postorderTraverse(node.left);
    postorderTraverse(node.right);
    postorder.push(node.idx);
  };

  preorderTraverse(root);
  postorderTraverse(root);

  return [preorder, postorder];
}
