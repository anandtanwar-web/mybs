import sys, getopt

def monkey_trouble(a_smile, b_smile):
    print("I am in a function")
    if a_smile=='True' and b_smile=='True':
        return True
    if a_smile !='True' and b_smile !='True':
        return True
    return False    

def getoptions():
    arglen=len(sys.argv)
    if arglen<2:
        print("invalid number of arguments")
        print ("use -h or --help")
        sys.exit()
        #Getting the list of Arguments and assinging it to opts
    try:
        opts, args =getopt.getopt(sys.argv[1:], "ha:b:", ["help", "weeekday", "vacation"])
    except  getopt.GetoptError:
            print("invalid arguments e.g. sleep_in0.py -a True -b True")
            sys.exit(2)
    for opt, args in opts:
        if opt in ("-h", "--help"):
            print (" please use argument -a for a_smile and -b for b_smile")
            print("usage e.g.: sleep_in0.py -a True -b False ")
            sys.exit()
        if opt in ("-a", "--asmile"):
            a_smile=args
        if opt in ("-b", "--bmsile"):
            b_smile=args
        if opt not in ("-h","-a", "-b", "--help", "--asmile", "--bsmile"):
            print ("invalid arguments")
            sys.exit()
    return a_smile, b_smile

if __name__=='__main__':
    arglist=getoptions()
    trouble_status=monkey_trouble(arglist[0], arglist[1])
    print("Am I in Trouble", trouble_status)
