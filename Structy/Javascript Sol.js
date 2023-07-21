const isPrime = (n) => {
    if (n < 2) return false;

    for (let i = 2; i <= Math.sqrt(n); i += 1) {
        if (n % i === 0) return false;
    }

    return true;
};


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


// compress
def compress(s):
    s += '!'
result = []
i = 0
j = 0
while j < len(s):
    if s[i] == s[j]:
    j += 1
else :
    num = j - i
if num == 1:
    result.append(s[i])
else :
    result.append(str(num))
result.append(s[i])
i = j

return ''.join(result)


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
