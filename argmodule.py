import argparse 

parser = argparse.ArgumentParser()
#positional args
parser.add_argument("a",type=int, help="first num")
parser.add_argument("b",type=int, help="second num")

#optional args
parser.add_argument("-a","--action", help="what operation to do with nums?")


args = parser.parse_args()
print(args)

def plus(a,b):
    print(a+b)

def minus(a,b):
    print(a-b)

if args.action =="plus":
    plus(args.a,args.b)
elif args.action=="minus":
    minus(args.a,args.b)
