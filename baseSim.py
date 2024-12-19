import numpy as np
import math;

        
#Simulation 2.0 was originally going to inherit 3d sim above but it had too many problems
class Sim2D:

    #initializing sim
    def __init__(self, x, y, gridlength, E, U, O, step) -> None:
        #initializes constants
        #NOTE: E, O, and U are treated as scarlar fields
        #E: permitivity
        #U: permeability
        #O: conductivity
        self.STEP = step
        self.GRIDLENGTH = gridlength
        self.XNUMBER = x
        self.YNUMBER = y

        #initializes electic and magnetic fields
        self.electricX = np.zeros((x, y))
        self.electricY = np.zeros((x, y))
        self.electricZ = np.zeros((x, y))
        self.magneticX = np.zeros((x, y))
        self.magneticY = np.zeros((x, y))
        self.magneticZ = np.zeros((x, y))

        #initializes electric field partials
        self.electricXX = np.zeros((x, y))
        self.electricXY = np.zeros((x, y))
        self.electricXZ = np.zeros((x, y))
        self.electricYX = np.zeros((x, y))
        self.electricYY = np.zeros((x, y))
        self.electricYZ = np.zeros((x, y))
        self.electricZX = np.zeros((x, y))
        self.electricZY = np.zeros((x, y))
        self.electricZZ = np.zeros((x, y))

        #initializes magnetic field partials
        self.magneticXX = np.zeros((x, y))
        self.magneticXY = np.zeros((x, y))
        self.magneticXZ = np.zeros((x, y))
        self.magneticYX = np.zeros((x, y))
        self.magneticYY = np.zeros((x, y))
        self.magneticYZ = np.zeros((x, y))
        self.magneticZX = np.zeros((x, y))
        self.magneticZY = np.zeros((x, y))
        self.magneticZZ = np.zeros((x, y))

        #initializes E, U, and O
        self.E = E
        self.U = U
        self.O = O
    
    #Updates partial derivatives
    def calcPartials(self, time) -> None:
        #Note: any partial with respect to Z should be zero since it is assumed that Z is unchanging
        self.electricXX = np.gradient(self.electricX, axis=0) / self.GRIDLENGTH
        self.electricXY = np.gradient(self.electricX, axis=1) / self.GRIDLENGTH
        self.electricYX = np.gradient(self.electricY, axis=0) / self.GRIDLENGTH
        self.electricYY = np.gradient(self.electricY, axis=1) / self.GRIDLENGTH
        self.electricZX = np.gradient(self.electricZ, axis=0) / self.GRIDLENGTH
        self.electricZY = np.gradient(self.electricZ, axis=1) / self.GRIDLENGTH

        self.magneticXX = np.gradient(self.magneticX, axis=0) / self.GRIDLENGTH
        self.magneticXY = np.gradient(self.magneticX, axis=1) / self.GRIDLENGTH
        self.magneticYX = np.gradient(self.magneticY, axis=0) / self.GRIDLENGTH
        self.magneticYY = np.gradient(self.magneticY, axis=1) / self.GRIDLENGTH
        self.magneticZX = np.gradient(self.magneticZ, axis=0) / self.GRIDLENGTH
        self.magneticZY = np.gradient(self.magneticZ, axis=1) / self.GRIDLENGTH

        self.fixBoundaries(time)

    #running the simulation (implementation of maxwell's equations)
    #it is ready hahahahahHAHAHAHAH
    def iterate(self):
        #calculating rate of change for magnetic field
        bxChange = -self.electricZY #the differential equations (with partials to Z equaling 0)
        byChange = self.electricZX
        bzChange = self.electricXY - self.electricYX

        #calculating rate of change for electric field
        exChange = (self.magneticZY)/(self.E * self.U) - (self.O * self.electricX)/(self.E)
        eyChange = (-self.magneticZX)/(self.E * self.U) - (self.O * self.electricY)/(self.E)
        ezChange = (self.magneticYX - self.magneticXY)/(self.E * self.U) - (self.O * self.electricZ)/(self.E)


        #updating fields
        self.magneticX = self.magneticX + self.STEP * bxChange #Def of calc
        self.magneticY = self.magneticY + self.STEP * byChange
        self.magneticZ = self.magneticZ + self.STEP * bzChange
        self.electricX = self.electricX + self.STEP * exChange
        self.electricY = self.electricY + self.STEP * eyChange
        self.electricZ = self.electricZ + self.STEP * ezChange

    def getXLength(self):
        return self.GRIDLENGTH * self.XNUMBER
    
    def getYLength(self):
        return self.GRIDLENGTH * self.YNUMBER
    
    def getZLength(self):
        return self.GRIDLENGTH * self.ZNUMBER
    
    #This pins the edges of the grid to zero preventing bad boundary conditions from forming
    #This also fluctuates the x = 0 edges to create light waves
    def fixBoundaries(self, time):

        #fixing x = 0 (Section A on the chart) (This is where waves are generated) (time parameter used)
        self.electricYX[0, :] = math.cos(0.3*self.STEP*time)

        self.electricXY[:, self.YNUMBER-1] = 0
        self.electricXZ[:, self.YNUMBER-1] = 0
        self.electricYX[:, self.YNUMBER-1] = 0
        self.electricYZ[:, self.YNUMBER-1] = 0
        self.electricZX[:, self.YNUMBER-1] = 0
        self.electricZY[:, self.YNUMBER-1] = 0

        self.electricXY[:, 0] = 0
        self.electricXZ[:, 0] = 0
        self.electricYX[:, 0] = 0
        self.electricYZ[:, 0] = 0
        self.electricZX[:, 0] = 0
        self.electricZY[:, 0] = 0

        self.electricXY[self.XNUMBER-1, :] = 0
        self.electricXZ[self.XNUMBER-1, :] = 0
        self.electricYX[self.XNUMBER-1, :] = 0
        self.electricYZ[self.XNUMBER-1, :] = 0
        self.electricZX[self.XNUMBER-1, :] = 0
        self.electricZY[self.XNUMBER-1, :] = 0
        
        





