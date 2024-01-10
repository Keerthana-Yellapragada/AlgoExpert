const isPrime = (n) => {
  if (n < 2) return false;

  for (let i = 2; i <= Math.sqrt(n); i += 1) {
    if (n % i === 0) return false;
  }

  return true;
};

// *********************************************************

// uncompress
const uncompress = (s) => {
  let result = [];
  const numbers = "0123456789";
  let i = 0;
  let j = 0;
  while (j < s.length) {
    if (numbers.includes(s[j])) {
      j += 1;
    } else {
      const num = Number(s.slice(i, j));
      for (let count = 0; count < num; count += 1) {
        result.push(s[j]);
      }
      j += 1;
      i = j;
    }
  }
  return result.join("");
};

// *********************************************************
// compress
const compress = (s) => {
  let result = [];
  let i = 0;
  let j = 0;

  while (j <= s.length) {
    if (s[i] === s[j]) {
      j += 1;
    } else {
      const num = j - i;
      if (num === 1) {
        result.push(s[i]);
      } else {
        result.push(String(num), s[i]);
      }
      i = j;
    }
  }

  return result.join("");
};

// *********************************************************
// Anagram
const anagrams = (s1, s2) => {
  const count = {};
  for (let char of s1) {
    if (!(char in count)) {
      count[char] = 0;
    }
    count[char] += 1;
  }

  for (let char of s2) {
    if (count[char] === undefined) {
      return false;
    } else {
      count[char] -= 1;
    }
  }

  for (let char in count) {
    if (count[char] !== 0) {
      return false;
    }
  }

  return true;
};

// *********************************************************
// Most Frequent Char

const mostFrequentChar = (s) => {
  let counter = {};

  for (let letter of s) {
    if (counter[letter] === undefined) {
      counter[letter] = 1;
    } else {
      counter[letter]++;
    }
  }

  let mostFreq = 0;
  let mostFreqLetter;

  for (let letter in counter) {
    if (counter[letter] > mostFreq) {
      mostFreqLetter = letter;
      mostFreq = counter[letter];
    }
  }

  return mostFreqLetter;
};
// *********************************************************

const intersection = (a, b) => {
  // todo
  const set = new Set();
  let result = [];
  for (let item of a) {
    if (!set.has(item)) {
      set.add(item);
    }
  }
  for (let item of b) {
    if (set.has(item)) {
      result.push(item);
    }
  }
  return result;
};

const fiveSort = (nums) => {
  let i = 0;
  let j = nums.length - 1;
  while (i < j) {
    if (nums[j] === 5) {
      j -= 1;
    } else if (nums[i] === 5) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i += 1;
    } else {
      i += 1;
    }
  }

  return nums;
};

const pairedParentheses = (str) => {
  let count = 0;

  for (let char of str) {
    if (char === "(") {
      count += 1;
    } else if (char === ")") {
      if (count === 0) {
        return false;
      }

      count -= 1;
    }
  }

  return count === 0;
};

const insertNode = (head, value, index) => {
  if (index === 0) {
    const newHead = new Node(value);
    newHead.next = head;
    return newHead;
  }

  let count = 0;
  let current = head;
  while (current !== null) {
    if (count === index - 1) {
      const next = current.next;
      current.next = new Node(value);
      current.next.next = next;
    }

    count += 1;
    current = current.next;
  }
  return head;
};

const longestStreak = (head) => {
  let maxStreak = 0;
  let currentStreak = 0;
  let currentNode = head;
  let prevVal = null;

  while (currentNode !== null) {
    if (currentNode.val === prevVal) {
      currentStreak += 1;
    } else {
      currentStreak = 1;
    }

    if (currentStreak > maxStreak) {
      maxStreak = currentStreak;
    }

    prevVal = currentNode.val;
    currentNode = currentNode.next;
  }

  return maxStreak;
};

const mergeLists = (head1, head2) => {
  if (head1 === null && head2 === null) return null;
  if (head1 === null) return head2;
  if (head2 === null) return head1;

  if (head1.val < head2.val) {
    const next1 = head1.next;
    head1.next = mergeLists(next1, head2);
    return head1;
  } else {
    const next2 = head2.next;
    head2.next = mergeLists(head1, next2);
    return head2;
  }
};

const zipperLists = (head1, head2) => {
  if (head1 === null && head2 === null) return null;
  if (head1 === null) return head2;
  if (head2 === null) return head1;
  const next1 = head1.next;
  const next2 = head2.next;
  head1.next = head2;
  head2.next = zipperLists(next1, next2);
  return head1;
};

const reverseList = (head, prev = null) => {
  if (head === null) return prev;
  const next = head.next;
  head.next = prev;
  return reverseList(next, head);
};

// DFS
const depthFirstValues = (root) => {
  if (root === null) return [];

  const values = [];
  const stack = [root];

  while (stack.length > 0) {
    const node = stack.pop();
    values.push(node.val);

    if (node.right !== null) stack.push(node.right);

    if (node.left !== null) stack.push(node.left);
  }

  return values;
};

// recursive DFS
const depthFirstValuesRecursive = (root) => {
  if (root === null) return [];

  const leftValues = depthFirstValues(root.left);
  const rightValues = depthFirstValues(root.right);

  return [root.val, ...leftValues, ...rightValues];
};

// BFS- BINARY TREE
const breadthFirstValues = (root) => {
  //    empty tree
  if (root === null) return [];
  //   fifo
  let queue = [root];
  let values = [];

  while (queue.length > 0) {
    let currNode = queue.shift();
    values.push(currNode.val);

    if (currNode.left !== null) queue.push(currNode.left);
    if (currNode.right !== null) queue.push(currNode.right);
  }

  return values;
};

// Sum of binary tree

// sum-BFS
const treeSum = (root) => {
  // todo

  if (root === null) return 0;
  let queue = [root];
  let sum = 0;

  while (queue.length > 0) {
    let curr = queue.shift();
    sum += curr.val;

    if (curr.left !== null) queue.push(curr.left);
    if (curr.right !== null) queue.push(curr.right);
  }
  return sum;
};

// DFS
const treeSumDFS = (root) => {
  if (root === null) return 0;

  let sum = 0;

  return root.val + treeSum(root.left) + treeSum(root.right);
};

// BT target
const treeIncludes = (root, target) => {
  // todo
  if (root === null) return false;
  if (root.val === target) return true;
  return treeIncludes(root.left, target) || treeIncludes(root.right, target);
};

//  BT- min value

// recursive sol
const treeMinValueRecursive = (root) => {
  // todo
  if (root === null) return Infinity;
  const smallestLeft = treeMinValue(root.left);
  const smallestRight = treeMinValue(root.right);

  return Math.min(root.val, smallestRight, smallestRight);
};

// iterative
const treeMinValue = (root) => {
  const stack = [root];

  let smallest = Infinity;
  while (stack.length) {
    const current = stack.pop();
    if (current.val < smallest) smallest = current.val;

    if (current.left !== null) stack.push(current.left);
    if (current.right !== null) stack.push(current.right);
  }
  return smallest;
};

// bfs iterative
const treeMinValueBFS = (root) => {
  const queue = [root];

  let smallest = Infinity;
  while (queue.length) {
    const current = queue.shift();
    if (current.val < smallest) smallest = current.val;

    if (current.left !== null) queue.push(current.left);
    if (current.right !== null) queue.push(current.right);
  }
  return smallest;
};

//  Max root to leaf sum

const maxPathSum = (root) => {
  if (root === null) return -Infinity;
  if (root.left === null && root.right === null) return root.val;
  return root.val + Math.max(maxPathSum(root.left), maxPathSum(root.right));
};

// tree path finder
const pathFinder = (root, target) => {
  if (root === null) return null;
  if (root.val === target) return [root.val];

  const leftPath = pathFinder(root.left, target);
  if (leftPath !== null) return [root.val, ...leftPath];

  const rightPath = pathFinder(root.right, target);
  if (rightPath !== null) return [root.val, ...rightPath];

  return null;
};

// Tree count

const treeValueCountRecursive = (root, target) => {
  if (root === null) return 0;
  const match = root.val === target ? 1 : 0;
  return (
    match +
    treeValueCount(root.left, target) +
    treeValueCount(root.right, target)
  );
};

const treeValueCount = (root, target) => {
  if (root === null) return 0;

  let count = 0;
  const stack = [root];
  while (stack.length > 0) {
    const current = stack.pop();
    if (current.val === target) count += 1;

    if (current.left) stack.push(current.left);
    if (current.right) stack.push(current.right);
  }

  return count;
};

//  how high
const howHigh = (node) => {
  if (node === null) return -1;

  const leftHeight = howHigh(node.left);
  const rightHeight = howHigh(node.right);
  return 1 + Math.max(leftHeight, rightHeight);
};



//  tree path finder
const TreepathFinder = (root, target) => {
  if (root === null) return null;
  if (root.val === target) return [root.val];

  const leftPath = TreepathFinder(root.left, target);
  if (leftPath !== null) return [root.val, ...leftPath];

  const rightPath = TreepathFinder(root.right, target);
  if (rightPath !== null) return [root.val, ...rightPath];

  return null;
};


const pathFinder = (root, target) => {
  const result = pathFinderHelper(root, target);
  if (result === null) {
    return null;
  } else {
    return result.reverse();
  }
};

const TreepathFinderHelper = (root, target) => {
  if (root === null) return null;
  if (root.val === target) return [root.val];

  const leftPath = TreepathFinderHelper(root.left, target);
  if (leftPath !== null) {
    leftPath.push(root.val);
    return leftPath;
  }

  const rightPath = TreepathFinderHelper(root.right, target);
  if (rightPath !== null) {
    rightPath.push(root.val);
    return rightPath;
  }

  return null;
};

// subsets
const subsets = (elements) => {
  if (elements.length === 0) return [
    []
  ];

  const ele = elements[0];
  const remainingElements = elements.slice(1);
  const subsetsWithoutEle = subsets(remainingElements);
  const subsetsWithEle = subsetsWithoutEle.map((sub) => [ele, ...sub]);
  return [...subsetsWithoutEle, ...subsetsWithEle];
};


//  permutations
// recursive sol
const permutations = (items) => {
  if (items.length === 0) return [
    []
  ];

  const first = items[0];
  const perms = permutations(items.slice(1));

  const fullPermutations = [];
  for (let perm of perms) {
    for (let i = 0; i <= perm.length; i += 1) {
      fullPermutations.push([...perm.slice(0, i), first, ...perm.slice(i)]);
    }
  }
  return fullPermutations;
};





// create combinations

const createCombinations = (items, k) => {
  if (items.length < k) return [];


  if (k === 0) return [
    []
  ];


  const first = items[0];
  const combosWithFirst = [];
  for (let combo of createCombinations(items.slice(1), k - 1)) {
    combosWithFirst.push([first, ...combo]);
  }

  const combosWithoutFirst = createCombinations(items.slice(1), k);
  return [...combosWithFirst, ...combosWithoutFirst];
};
