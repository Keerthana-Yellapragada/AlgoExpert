

# SOLUTIONS

# *************************************************************************
# #   VALID PALINDROME

# class Solution(object):
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2 pointers
        new_string = ""


        for letter in s:
            if letter.isalnum():
                new_string += letter.lower()

        l=0
        r=len(new_string) - 1

        print(new_string)
        print(r)
        #  saas
        # l=2
        # r=1
        while l <= r:
            if new_string[l] == new_string[r]:
               l = l+1
               r = r-1
            else:
               return False

        return True


#  def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # x = txt.isalnum()

#         # create a new empty string
#         # we iterate over given string after converting to lowercase and check if alphanum
#         # if yes,push to new string
#         # iterate backwards and push into another new string
#         #  check if its the same as original's lowercase
#         #  if yes,return true

#         new_string = ""
#         reversed_string = ""

#         for letter in s:
#             if letter.isalnum():
#                 new_string += letter.lower()

#         for i in range(len(new_string), -1):
#             reversed_string += new_string[i]

#         #  return new_string == reversed(new_string)
#         #  return new_string == new_string.reversed()
#         print(new_string)
#         print(reversed_string)
#         return new_string == reversed_string

#  def isPalindrome(self, s):
#      """
#         :type s: str
#         :rtype: bool
#         """
#      # x = txt.isalnum()

#      # create a new empty string
#      # we iterate over given string after converting to lowercase and check if alphanum
#      # if yes,push to new string
#      # iterate backwards and push into another new string
#      #  check if its the same as original's lowercase
#      #  if yes,return true

#      new_string = ""
#       reversed_string = ""

#        for letter in s:
#             if letter.isalnum():
#                 new_string += letter.lower()

#         for i in range(len(new_string)-1, -1, -1):
#             # range(start, stop, step)
#             reversed_string += new_string[i]

#         #  return new_string == reversed(new_string)
#         #  return new_string == new_string.reversed()
#         print(new_string)
#         print(reversed_string)
#         return new_string == reversed_string


# *************************************************************************



#  2 SUM SORTED INPUT ARRAY

def twoSum2(arr, target):
    l, r = 0, len(arr) - 1
    while (l < r):
        if (arr[l] + arr[r] > target):
            r -= 1
        if (arr[l] + arr[r] < target):
            l += 1
        if (arr[l] + arr[r] == target):
            return [l, r]


print(twoSum2([1, 3, 4, 5, 7, 10, 11], 9))
# *************************************************************************



#  3 SUM
def threeSum(self, nums):
    result = []
    nums.sort()

    for i in range(len(nums)):
        print("i is", i)
        l = i+1
        r = len(nums)-1
        while (l < r):
            print("i, l, r", i, l, r)
            if (nums[i] + nums[l] + nums[r] > 0):
                r = r-1
            elif (nums[i] + nums[l] + nums[r] < 0):
                l = l+1
            else:
                if [nums[i], nums[l], nums[r]] not in result:
                    result.append([nums[i], nums[l], nums[r]])
                l = l + 1
                r = r - 1

    return result
# *************************************************************************



# BUY AND SELL STOCK
def buySellStock2(arr):
    maxProfit = 0
    currProfit = 0
    l = 0
    r = l + 1

    while (r < len(arr)):
        if (arr[l] > arr[r]):
            l = r
            r += 1
        elif (arr[l] <= arr[r]):
            currProfit = arr[r] - arr[l]
            maxProfit = max(maxProfit, currProfit)
            r += 1

    return maxProfit

# def buySellStock(prices):
#     l, r = 0, 1
#     maxP = 0

#     while(r < len(prices)):
#         if(prices[l] < prices[r]):
#             profit = prices[r]-prices[l]
#             if(maxP < profit):
#                 maxP = profit
#             #maxP = max(maxP, profit)
#         else:
#             l = r
#         r+=1

#     return maxP

# print(buySellStock([7,1,5,3,6,4]))
# *************************************************************************



# did not work but passed some test cases

def longestRepeatingCharReplacement(str, k):
    l = 0
    r = 1
    count = 1
    maxCount = 0
    newStr = list(str)

    while(r < len(str)):
        if newStr[l] == newStr[r]:
            count+=1
            maxCount = max(maxCount, count)
        else:
            if k != 0:
                newStr[r] = newStr[l]
                k-=1
                count+=1
                maxCount = max(maxCount, count)
            else:
                l=r
                r=l+1
                count = 0

        r+=1
        l+=1


    return maxCount




# print(longestRepeatingCharReplacement("ABAB", 2)) #4
# print(longestRepeatingCharReplacement("AABABBA", 1)) #4

# *************************************************************************


# smallest contiguous subarray taht's greater than or equal to target

def minSizeSubArray(nums, target):
    length = 0
    minLength = float("inf")
    currSum = 0
    l=0
    r=0

    for i in range(len(nums)):

        if(currSum < target):
            l=i
            r=l+1
            currSum = nums[l]

            while(currSum < target and r<len(nums)):
                currSum+=nums[r]
                if(currSum < target):
                    r+=1
            length = r-l+1
            minLength = min(minLength, length)


    return minLength

# print(minSizeSubArray([2,3,1,2,4,3], 7))

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


# Next permutations
def nextPermutation(self, nums):
       for i in range(len(nums)-1, 0, -1):
            # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])

                # get the index before the last peak
                j = i - 1

                # swap the pre-last peak index with the value just large than it
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()



# 22. Generate Parentheses
def generateParenthesis(self, n: int) -> List[str]:

        def helper(ans, s, left, right):
            if left==0 and right==0:
                ans.append(s)

            if left>0:
                helper(ans, s+'(', left-1, right)

            if right>0 and left<right:
                helper(ans, s+')', left, right-1)

        ans = []
        helper(ans, '', n, n)

        return ans


# 24. Swap Nodes in Pairs

def swapPairs(self, head: ListNode) -> ListNode:

        dummy = prev = ListNode(0)
        prev.next = head

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next


# Roman to Integer
def romanToInt(self, s: str) -> int:

        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number-=roman[s[i]]
            else:
                number+=roman[s[i]]
        return number+roman[s[-1]]


def romanToInt(self, s: str) -> int:

        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }


        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))



# 69. Sqrt(x)

def mySqrt(self, x: int) -> int:
        number=1
        while number*number<=x:
            number+=1
        return number

    # binary search approach:
    #  def mySqrtBinary(self, x: int) -> int:
    #     left,right=1,x
    #     while left<=right:
    #         mid=(left+right)//2
    #         if mid*mid==x:
    #             return mid
    #         if mid*mid>x:
    #             right=mid-1
    #         else:
    #             left=mid+1
    #     return right


# Linked List Cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize two pointers to the head of the linked list
        slow = head
        fast = head

        # Traverse the linked list using the slow and fast pointers
        while fast and fast.next:
        # Move the slow pointer one node at a time
            slow = slow.next

        # Move the fast pointer two nodes at a time
            fast = fast.next.next

        # If the fast pointer ever equals the slow pointer, then there is a cycle
            if slow == fast:
                return True

        # If we have reached the end of the linked list, then there is no cycle
        return False




# # twoSum
# def twoSum(self, nums, target):

#         #  index are stored as dict valuse, nums are keys
#         numsObj = {}
#         for i,n in enumerate(nums):
#             diff = target - n
#             if diff in numsObj:
#                 return [numsObj[diff], i]
#                 #  indices of numbers that add up to target
#             else:
#                 numsList[n] = i


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""

        for i in range(min(len(word1),len(word2))):
            result += word1[i] + word2[i]

        return res + word1[i+1:] + word[i+1:]
