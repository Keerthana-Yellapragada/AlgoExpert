from math
import sqrt, floor

def is_prime(n):
    if n < 2:
    return False

for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
    return False

return True


# uncompress
def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j

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
