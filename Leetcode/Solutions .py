
# #   VALID PALINDROME

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
