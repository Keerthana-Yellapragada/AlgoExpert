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

// PYTHON SOLUTION

// def isValidSubsequence(array, sequence):
//     sequenceIndex = 0

// for value in array:
//     if sequenceIndex == len(sequence):
//     break
// if sequence[sequenceIndex] == value:
//     sequenceIndex += 1
// return sequenceIndex == len(sequence)


// ********************************************************************************************
