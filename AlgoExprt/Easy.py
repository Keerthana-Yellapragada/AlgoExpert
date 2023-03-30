
# VALIDATE SUBSEQUENCE
def isValidSubsequence(array, sequence):

    sequenceIndex = 0
    for value in array:
        if sequenceIndex == len(sequence):
            break
        if sequence[sequenceIndex] == value:
            sequenceIndex += 1
    return sequenceIndex == len(sequence)


# ***************************************************
# Sorted Square Array
def sortedSquaredArray(array):
    return sorted([x**2 for x in array])

# ***************************************************
