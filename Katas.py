#The Kata file for modules


def even_or_odd(number):
    return "Even" if number%2==0 else "Odd"


def narcissistic( value ):
    sum = 0
    valStr = str(value)
    base = len(valStr)
    for index, x in enumerate(valStr):
      sum += int(x)**base
    return sum == value



def solution(string,markers):
    newStr = ""
    str = string.split("\n")
    for index,s in enumerate(str):
      for x in range(len(s)):
        c = s[x]
        if c in markers:
          break
        else:
          newStr += c
      newStr = newStr.strip()
      newStr.join("\n")
    return newStr


def connotation(strng):

  return True