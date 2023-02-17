"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
def sum_double(a, b):
  if a==b:
    sum=2*(a+b)
  else:
    sum=a+b
  return sum


  """
  Given an int n, return the absolute difference between n and 21,
  except return double the absolute difference if n is over 21.
  """
def diff21(n):
   if n<21:
    diff=21-n
   else:
    diff=2*(n-21)
   return diff


 """
  We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
 We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if
  we are in trouble.
  parrot_trouble(True, 6) → True
"""
def parrot_trouble(talking, hour):
  if (hour<7 or hour>20) and talking:
   return True
  else:
   return False



if __name__=='__main__':
    result=sum_double(2, 2)
    print("result is", result)
    result=sum_double(1, 2)
    print("result is", result)
    diff=diff21(30)
    print("diff21 is ", diff)
