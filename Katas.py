#The Kata file for modules
import re

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
    positive = negative = 0
    str2 = re.split(r"[\s]+", strng)

    for s in str2:
        if ord(s[0].lower()) < 110:
            positive += 1
        else:
            negative += 1
    return positive >= negative


def decode_pass(pass_list, bits):
    for passw in pass_list:
        temp = ' '.join(format(ord(c), '08b') for c in passw)
        if temp == bits:
            return passw
    return False

