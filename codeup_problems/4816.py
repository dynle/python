import sys
T = int(sys.stdin.readline())
if ((T%300)%60)%10 != 0:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(T//300)+" "+str((T%300)//60)+" "+str(((T%300)%60)//10))