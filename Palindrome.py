def pal(r):
    s = 0
    e = len(r)-1
     
    while e > s:
        if(r[s]!= r[e]):
            return False
        s+=1
        e-+1
    return True

    r = 123321

    if(pal(r)):
        print("This tuple is flip-flop")
    else:
        print("This tuple is not flip flop")
