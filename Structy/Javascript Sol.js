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
    const numbers = '0123456789';
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
    return result.join('');
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

    return result.join('');

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
    let counter = {}

    for (let letter of s) {
        if (counter[letter] === undefined) {
            counter[letter] = 1
        } else {
            counter[letter]++
        }
    }


    let mostFreq = 0;
    let mostFreqLetter;

    for (let letter in counter) {
        if (counter[letter] > mostFreq) {
            mostFreqLetter = letter
            mostFreq = counter[letter]
        }
    }



    return mostFreqLetter
};
// *********************************************************

const intersection = (a, b) => {
    // todo
    const set = new Set()
    let result = []
    for (let item of a) {
        if (!set.has(item)) {
            set.add(item)
        }
    }
    for (let item of b) {
        if (set.has(item)) {
            result.push(item)
        }
    }
    return result
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
        if (char === '(') {
            count += 1;
        } else if (char === ')') {
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
