import sys

if(len(sys.argv) > 1):
    if(int(sys.argv[1]) > 1 and int(sys.argv[1]) < 50):
        print("Ok")
    else:
        print("Out of range")
