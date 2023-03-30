
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
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # 2 pointers
#         new_string = ""


#         for letter in s:
#             if letter.isalnum():
#                 new_string += letter.lower()

#         l=0
#         r=len(new_string) - 1

#         print(new_string)
#         print(r)
#         #  saas
#         # l=2
#         # r=1
#         while l <= r:
#             if new_string[l] == new_string[r]:
#                l = l+1
#                r = r-1
#             else:
#                return False

#         return True



#  2 SUM SORTED INPUT ARRAY


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
