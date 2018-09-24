for m in range(1,10):
    for k in range(1,m) :
         print (end="        \t")
    for n in range(m,10):
        print("%d*%d=%2d\t" % (m,n,m*n),end="")
    print("")
