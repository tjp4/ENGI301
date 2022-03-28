def move(t1,t2):
    #todo
    #make so given theta 1 & 2 it goes there
    return

def readG(string):
    #todo
    #given Gcode string output desired needed theta 1&2
    #we ignoring G01 vs G02 vs G03, ALL ASSUMED FAST INTERPOLATION
    return

def stepperMove(theta):
    #if i need, given some theta moves moter to there
    #might be redundant
    #good place to copypasta
    #could split into move motre 1 and 2 as seperate functions, keep pins sep

    return

#might need if statement for the pen conrotl, sum like "IF Z<0 then pen down"

#main void gon go like

#read file
#loop : read line, move
#repeat till done