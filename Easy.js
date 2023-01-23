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

//
