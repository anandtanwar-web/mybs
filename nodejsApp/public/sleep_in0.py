#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
import sys, getopt

#this is the sleep_in function
def sleep_in(weekday, vacation):
  if weekday=='False':
      print("Function vale of weekday is:",weekday)
      return 'True'
  elif vacation=='True':
      return 'True'
  else:
     return 'False'

#print("Number of arguments:",len(sys.argv),"arguments")
#checking length of arguments
arglen=len(sys.argv)
if arglen<2:
    print("invalid number of arguments")
    print ("use -h or --help")
    sys.exit()

#Getting the list of Arguments and assinging it to opts
try:
    opts, args =getopt.getopt(sys.argv[1:], "hw:v:", ["help", "weeekday", "vacation"])
except  getopt.GetoptError:
        print("invalid arguments e.g. sleep_in0.py -w True -v False")
        sys.exit(2)

#looping opts for argument assignment and script usage
for opt, args in opts:
    if opt in ("-h", "--help"):
        print (" please use argument -w for weekday and -v for vacation")
        print("usage e.g.: sleep_in0.py -w True -v False ")
        sys.exit()
    if opt in ("-w", "--weekday"):
        weekday=args
    if opt in ("-v", "--vacation"):
        vacation=args
    if opt not in ("-h","-v", "-w", "--help", "--vacation", "weekday"):
        print ("invalid arguments")
        sys.exit()


#weekday=sys.argv[1]
#vacation=sys.argv[2]

print("Weekeday is:", weekday,"vacation is:", vacation)
output=sleep_in(weekday,vacation)
print("Are we sleeping in", output)
