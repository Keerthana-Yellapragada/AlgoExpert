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
