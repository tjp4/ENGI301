PLOTTER PROJECT

Takes input GCODE from file gcodeTest.txt
running movement.py will prompt the user to zero the arm
this will stop holding the torque of the plotter arm and allow the user to zero the arm
then once done pressing enter or any key will allow the arm to start plotting

any positive or zero valued Z axis input will be interpreted as putting the pen up and not writing
any negative valued Z input will put the pen down and start writing

the code only supports linear interpolation (G01) and direct movement (G00), circular interpolation will be interpreted as linear
the code also only accepts units of mm, and will not respond to unit changes (G20 / G21)

-Tyler Pitts
ENGI301 
2022