import kinematics
import stepperMove
import time
import math


gCode = []
with open("gcodeTest.txt") as f:
    gCode = f.readlines()

#------------------------------adddddd ZERO THING FROM STEPPER MOVE
stepperMove.zero()

xPrev = 100
yPrev = 100
zPos = 0
th1 = 0
th2 = 0

for G in gCode:             #all units always mm, IGNORE G21, ONLY CARE MOVEMENT G0#
    if (G[0] == 'G' and G[1] == '0'):
        G = G.replace(" ","")
        moveType = G[2]
        xInd = G.find('X')
        yInd = G.find('Y')
        zInd = G.find('Z')
        fInd = G.find('F')
        iInd = G.find('I')
        if (fInd==-1):
            fInd = 1000
        if (iInd==-1):
            iInd=1000
        end = min(fInd,iInd)

        xPos = xPrev
        yPos = yPrev
        if (xInd>0):
            xPos = float(G[(xInd+1):(yInd)])+100
            yPos = float(G[(yInd+1):(zInd)])+100
        
        if (zInd>0):
            zPos = float(G[(zInd+1):end])
        
        #------------------ NOW HAVE xPos yPos zPos and moveType
        #move type can be 0,1,2,3 FOR NOW IGNORING 123, ALL linear interp
        
        stepperMove.pen(zPos) #servo up/down
        
        #add movetype differentation
        if (moveType==0):
            thDes = kinematics.ik(xPos,yPos)
            stepperMove.m1(th1,thDes[0],1)
            stepperMove.m2(th2,thDes[1],.5)
            th1 = kinematics.deg2step(thDes[0])*1.8
            th2 = kinematics.deg2step(thDes[1])*1.8
            time.sleep(.2)
        else:
            xDist = xPos-xPrev
            yDist = yPos-yPrev
            n = round(math.sqrt(xDist**2+yDist**2))
            for j in range(0,n):
                xPos = xDist*j/n+xPrev
                yPos = yDist*j/n+yPrev
                print(xPos,yPos)
                thDes = kinematics.ik(xPos,yPos)
                stepperMove.m1(th1,thDes[0],1)
                stepperMove.m2(th2,thDes[1],.5)
                th1 = kinematics.deg2step(thDes[0])*1.8
                th2 = kinematics.deg2step(thDes[1])*1.8
                time.sleep(.2)
        xPrev = xPos
        yPrev = yPos
        zPrev = zPos