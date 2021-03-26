#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
import sys

def sleep_in(weekday, vacation):
  if weekday=='False':
      print("Function vale of weekday is:",weekday)
      return 'True'
  elif vacation=='True':
      return 'True'
  else:
     return '   False'

print("Number of arguments:",len(sys.argv),"arguments")
weekday=sys.argv[1]
vacation=sys.argv[2]
print("Weekeday is:", weekday,"vacation is:", vacation)
output=sleep_in(weekday,vacation)
print("Are we sleeping in", output)
