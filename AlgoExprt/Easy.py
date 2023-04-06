
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


# *************************************************************************


# remove duplicates from a linked list:

# # This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):

    currNode = linkedList

    while (currNode.next is not None):
        if currNode.value == currNode.next.value:
            currNode.next = currNode.next.next
        else:
            currNode = currNode.next

    return linkedList
