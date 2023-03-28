//  TWO NUMBER SUM
function twoNumberSum(array, targetSum) {
    // Write your code here.
    let newArray = []

    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] + array[j] === targetSum) {
                newArray.push(array[i], array[j])
            }
        }
    }

    return newArray;
}

// ****************************************************************

// VALIDATE SUBSEQUENCE

function isValidSubsequence(array, sequence) {
    let arrayIndex = 0
    let sequenceIndex = 0

    while (arrayIndex < array.length && sequence < sequence.length) {
        if (array[arrayIndex] == sequence[sequenceIndex]) {
            sequenceIndex++
        }
        arrayIndex++
    }

    //  if we have succesfully traversed the array, then the subsequence was found
    return sequenceIndex == sequence.length
}



// ********************************************************************************************

//  ISPALINDROME
function isPalindrome(string) {
    let reversed = ""

    for (let i = string.length - 1; i >= 0; i--) {
        reversed += string[i]
    }

    return reversed === string
}

// ********************************************************************************************ow t

//  CAESER'S CIPHER
