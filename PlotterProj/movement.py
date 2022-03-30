import kinematics
#import stepperMove


gCode = []
with open("C:/Users/pitts/Documents/GitHub/ENGI301/PlotterProj/gcodeTest.txt") as f:
    gCode = f.readlines()

#------------------------------adddddd ZERO THING FROM STEPPER MOVE
xPos = 0
yPos = 0
zPos = 0
th1 = 0
th2 = 0

for G in gCode:             #all units always mm, IGNORE G21, ONLY CARE MOVEMENT G0#
    xPrev = xPos
    yPrev = yPos
    zPrev = zPos

    if (G[0] == 'G' and G[1] == '0'):
        G = G.replace(" ","")
        moveType = G[2]
        xInd = G.find('X')
        yInd = G.find('Y')
        zInd = G.find('Z')
        fInd = G.find('F')
        iInd = G.find('I')
        
        end = max(fInd,iInd)

        xPos = xPrev
        yPos = yPrev
        zPos = zPrev
        if (xInd>0):
            xPos = G[(xInd+1):(yInd)]
            yPos = G[(yInd+1):(zInd)]
        
        if (zInd>0):
            zPos = G[(zInd+1):end]
        
        #------------------ NOW HAVE xPos yPos zPos and moveType
        #move type can be 0,1,2,3 FOR NOW IGNORING 123, ALL linear interp
        if (zPos<0):
            #add servo mvmnt
            print("servo down")
        
        #add movetype differentation
        thDes = kinematics.ik(xPos,yPos)
        #m1(curr,desireed,somespd)
        th1 = kinematics.deg2step(thDes[0])*1.8
        th2 = kinematics.deg2step(thDes[1])*1.8
        

