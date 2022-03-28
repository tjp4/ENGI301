import math
from turtle import end_fill

l1 = 1
l2 = 1

def fk(t1,t2):              #theta1 is joint 1, theta 2 is joint 2 wrt joint1 CURRENTLY IN DEG
    th1 = t1*math.pi/180
    th2 = t2*math.pi/180

    x = l1*math.cos(th1)+l2*math.cos(th1+th2)
    y = l1*math.sin(th1)+l2*math.sin(th1+th2)

    out = [x,y]
    return(out)
    
def ik(x,y):
    psi = math.acos((x**2+y**2+l1**2-l2**2)/(2*l1*math.sqrt(x**2+y**2)))
    b = math.atan2(x,y)

    th2 = abs(math.acos((x**2+y**2-l1**2-l2**2)/(2*l1*l2)))  #currently using positive theta2, negative theta1, flip if need
    th1 =b-psi

    th1 = th1*180/math.pi   #convert to deg
    th2 = th2*180/math.pi   #convert to deg

    out = [th1,th2]
    
    return(out)

print(ik(1,1))