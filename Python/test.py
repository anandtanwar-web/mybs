def missing_char(str, n):
  length=len(str)
  print(length)
  strs=''
  for l in range(length):
    if l==n:
       continue
    else:
       strs=strs+str[l]
    l=l+1
  return strs

def mis_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

if __name__ == '__main__':
      result=missing_char("kittens", 1)
      print(result)
