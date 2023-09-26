from math
import sqrt
import floor


def is_prime(n):
    if n < 2:
    return False


for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
    return False

return True


# uncompress
def uncompress(s):

    #  loop through main string
    #  divide into groups

    #  two pointers start at first character of string ( i, j) = 0
    # increment j until isalpha(string[j]) === true
    # add string[i] till string[j-1] to a varible called "numberreps"
    #  print out string[j] 'numberreps' amount of times
    # increment j + 1
    #  reset i to equal j
    #  repeat process

    i = 0
    j = 0
# 12y25h
    result = []
    for charac in s:

        #      if charac is alphabet, then we stop and print
        if charac.isalpha() is True:

            num_reps = ''
#       '12'

            while i < j:
                print("S at i :", s[i])
                num_reps += s[i]
                i += 1

            letter = s[j]
            totalreps = int(num_reps)

            result.append(letter * totalreps)

#   reset
            j += 1
            i = j

#    if char is a number, we move the second pointer (first pointer doesn't move because it marks the beginning)
        else:
            j += 1

    return ''.join(result)


# compress
def compress(s):
    s += '!'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num))
                result.append(s[i])
            i = j

    return ''.join(result)


# ************************************************************************************
# anagrams

def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)


def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count


#  most frequest char
def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best


# pair sum


def pair_sum(numbers, target_sum):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_numbers:
            return (index, previous_numbers[complement])

        previous_numbers[num] = index


# pair product

def pair_product(numbers, target_product):
    previous_nums = {}

    for index, num in enumerate(numbers):
        complement = target_product / num

        if complement in previous_nums:
            return (index, previous_nums[complement])

        previous_nums[num] = index


# Anagram
def anagrams(s1, s2):

    return Counter(s1) == Counter(s2)


def pair_sum(numbers, target_sum):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_numbers:
            return (index, previous_numbers[complement])

        previous_numbers[num] = index


def pair_product(numbers, target_product):
  previous_nums = {}

  for index, num in enumerate(numbers):
    complement = target_product / num

    if complement in previous_nums:
      return (index, previous_nums[complement])

    previous_nums[num] = index


def intersection(a, b):
  result = []

  for item in b:
    if item in a:
      result.append(item)
  return result


def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while i < j:
    if nums[j] == 5:
       j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums


def paired_parentheses(string):
  count = 0

  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1

  return count == 0



# LINKED LISTS


def linked_list_values(head):
  values_list = []

  curr = head

  while curr is not None:

    values_list.append(curr.val)

    curr=curr.next
  return values_list
