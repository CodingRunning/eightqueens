#!/usr/bin/python

def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False

def queens(num=8,state=()):
    print "in queens, now state=",state
    if len(state)==num-1:
        for pos in range(num):
            print "in queens, state=",state,", pos=",pos
            if not conflict(state,pos):
                print "in queens if, not conflict pos=",pos
                yield (pos,)
    else:
        for pos in range(num):
            print "in queess else, state=",state,", pos=",pos
            if not conflict(state,pos):
                for result in queens(num,state+(pos,)):
                    print "in queens else, pos=",pos,"result=",result
                    print "in queens else, (pos,)+result=",(pos,)+result
                    yield (pos,)+result

print list(queens(8))


