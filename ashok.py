x = int(input())
initial = list(input().split())
forces = list(map(int,input().split()))
if initial[1]=='Right':
    initial_val = int(initial[0])
if initial[1]=='Left':
    initial_val = 0-int(initial[0])
def fun1(currentforceindex,totalforce,direction):
    if direction=='l':
        totalforce = totalforce-forces[currentforceindex]
        if totalforce==0:
            return 1
        if len(forces)-1==currentforceindex:
            return 0
        return fun1(currentforceindex+1,totalforce,'l') or fun1(currentforceindex+1,totalforce,'r')
    if direction=='r':
        totalforce += forces[currentforceindex]
        if totalforce==0:
            return 1
        if len(forces)-1==currentforceindex:
            return 0
        return fun1(currentforceindex+1,totalforce,'l') or fun1(currentforceindex+1,totalforce,'r')
        

x = fun1(0,initial_val,'l') or fun1(0,initial_val,'r')
if x ==1:
    print('Possible',end='')
else:
    print('Not Possible',end='')
