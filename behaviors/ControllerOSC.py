from operationscore.Behavior import * 
from logger import main_log
#import util.ColorOps as color 
import colorsys
from numpy import array
import pdb
import util.ComponentRegistry as compReg

speedfactor = 15
<<<<<<< HEAD
vel_decay = .01
=======
vel_decay = .00
>>>>>>> b67a37ad06fa4c97dcdb32cecc71c7f492b12840

def constrainLocation(v,c):
    if v[0] > c[0]:
        v[0] = c[0]
    elif v[0]<0:
        v[0] = 0
    
    if v[1] > c[1]:
        v[1] = c[1]
    elif v[1]<0:
        v[1] = 0

    return v

class ControllerOSC(Behavior):   
    def behaviorInit(self):
        self.xy = array((0,0))
        self.v_xy = array((0,0))
        self.v_decay = vel_decay

        self.start_hsv = [0,1,1] 
        self.dest_hsv = [0,1,1] 
        self.ssize = compReg.getComponent('Screen').getSize()[-2:] #896 x 310
    
    def processResponse(self, sensorInputs, recursiveInputs):
        ret = []
        if sensorInputs:
            data = sensorInputs[-1]#for data in sensorInputs:
            if data['Path'] == '/sixaxis/xy':
                #try:
                    x = data['Value'][0]
                    y = data['Value'][1]
<<<<<<< HEAD
=======
                    main_log.error(str(x))
>>>>>>> b67a37ad06fa4c97dcdb32cecc71c7f492b12840
                    if y < 0:
                        self.start_hsv[1] = 1.0+y #s
                    else:
                        self.start_hsv[2] = 1.0-y
                    self.start_hsv[0] = (x+1) * 180.0  
<<<<<<< HEAD
#                    if self.start_hsv[0] >= 360:
#                        self.start_hsv[0] = 0
#                    if self.start_hsv[0] <=0:
#                        self.start_hsv[0] = 360
#self.h = x * 360.
                    
                #except(e):
                #    pdb.set_trace()
            elif data['Path'] == '/sixaxis/lrud':
                val=data['Value']
                vy = val[3] if val[3] else -val[2]
                vx = -val[0] if val[0] else val[1]
=======
            elif data['Path'] == '/sixaxis/lrud':
                val=data['Value']
                vy = val[3]-val[2]
                vx = val[1]-val[0] 
>>>>>>> b67a37ad06fa4c97dcdb32cecc71c7f492b12840
                #pdb.set_trace()
                #self.v_xy = (val[1]*ssize[0], (1.0-val[0])*ssize[1])
                self.v_xy = array((vx, vy)) * speedfactor
            else:
                main_log.error('Sensor Inputs: ' + str(sensorInputs))
        self.xy = self.xy + self.v_xy
        constrainLocation(self.xy,self.ssize)
        self.v_xy -= self.v_decay
        if self.v_xy[0] < 0:
            self.v_xy[0] = 0
        if self.v_xy[1] < 0:
            self.v_xy[1] = 0
<<<<<<< HEAD
        ret.append({'Color':[i*256 for i in
        colorsys.hsv_to_rgb(*self.start_hsv)],'Location':(int(self.xy[0]), int(self.xy[1]))})
=======
        ret.append({'Color':[i*255 for i in colorsys.hsv_to_rgb(*self.start_hsv)],'Location':(int(self.xy[0]), int(self.xy[1]))})
>>>>>>> b67a37ad06fa4c97dcdb32cecc71c7f492b12840
    
        return (ret, [])
