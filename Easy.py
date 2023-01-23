
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
